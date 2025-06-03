class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
       
        s_nums = sorted(nums)
        ans = 0
        for i in range(0,len(nums), 2):
            ans += s_nums[i]
        
        return ans


        