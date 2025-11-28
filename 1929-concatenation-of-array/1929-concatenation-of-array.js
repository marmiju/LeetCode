/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    n = nums.length
    ans = new Array(n*2)

    for(let i=0; i<n; i++){
        ans[i] = nums[i]
        ans[i+n] = nums[i]
    }
    return ans
    
};