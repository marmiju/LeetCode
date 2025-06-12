class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        diff = abs(nums[-1] - nums[0])
        for i in range(1,len(nums)):
            diff = max(abs(nums[i] - nums[i-1]), diff)
        
        return diff


        