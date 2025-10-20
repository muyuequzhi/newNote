function computeYear(initVal, x, targetVal) {
  /**
   * 给定年收益率，计算多少时间金额可以翻倍
   * computeYear(100000, 0.1, 200000) => 8
   */
  for(var i=1;i<10000;i++) {
    initVal = initVal * (1 + x)
    console.log(initVal, i)
    if(initVal > targetVal) {
      return i
    }
  }
}

/**
 * 统计一个数组中每个元素出现的次数
 * count(['a','b','a','c','a']) =>  { a: 3, b: 1, c: 1 }
 */
function count(arr) {
  return arr.reduce((initVal, item)=> {
            initVal[item] == undefined ? initVal[item]=1  : initVal[item]+=1
            // 赋值后要返回初始值
            return initVal
          }, {})
}

function computeYear(initVal, x, targetVal, i) {
  /**
   * 给定年收益率，计算多少时间金额可以翻倍
   * computeYear(100000, 0.1, 200000, 0) => 214358.88100000017,8
   * initVal：初始金额
   * x：年收益率
   * targetVal：目标金额
   * i：计数初始值
   */
  
  initVal = initVal * (1 + x)
  i+=1
  console.log(initVal, i)
  if(initVal > targetVal) {

    return `${initVal}, i`
  } else {
    computeYear(initVal, x, targetVal,i)
  }
}



for(let i =8;i<19;i++){
  let s1 = `${i}:00`
  let s2 = `${i}:30`
  
  console.log(s1,s2) 
}