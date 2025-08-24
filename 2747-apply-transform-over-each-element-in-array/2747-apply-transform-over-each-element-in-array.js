/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let result = [];   //  empty array initialize
    for (let i = 0; i < arr.length; i++) {
        result[i] = fn(arr[i], i);  //  index এ value বসাচ্ছি
    }
    return result;
};
