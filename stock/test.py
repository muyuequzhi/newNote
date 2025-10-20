from flask import Flask, request, jsonify
from flask_cors import CORS
import akshare as ak
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# 定义数据保存目录
DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)  # 如果目录不存在则创建

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    data = request.get_json()
    stock_names = data.get('stock_names', [])
    start_date = data.get('start_date', '20240101')
    end_date = data.get('end_date', '20251001')

    stock_list_df = ak.stock_info_a_code_name()
    results = {}

    for name in stock_names:
        stock_row = stock_list_df[stock_list_df['name'] == name]
        if stock_row.empty:
            results[name] = {'error': '未找到股票名称'}
            continue

        stock_code = stock_row.iloc[0]['code']
        filename = os.path.join(DATA_DIR, f"{name}.csv")
        try:
            # 如果本地文件存在，优先读取
            if os.path.exists(filename):
                df = pd.read_csv(filename, encoding="utf-8-sig")
                print(f"📁 已读取本地缓存：{filename.replace(os.sep, '/')}")
            else:
                # 否则调用 AkShare 获取数据并保存
                df = ak.stock_zh_a_hist(
                    symbol=stock_code,
                    period="daily",
                    start_date=start_date,
                    end_date=end_date,
                    adjust="qfq"
                )
                df.to_csv(filename, index=False, encoding="utf-8-sig")
                print(f"✅ 已保存新数据：{filename.replace(os.sep, '/')}")

            # 返回前几行数据作为预览
            # results[name] = df.head(100).to_dict(orient='records')
            results[name] = df.to_dict(orient='records')

        except Exception as e:
            results[name] = {'error': str(e)}

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
