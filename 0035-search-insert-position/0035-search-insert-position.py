class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        freq = {}

        for i,val in enumerate(nums):
            freq[val] = i
            if i > 0 and nums[i] > target and nums[i-1]< target:
                return i 
        
        if target in freq:
            return freq[target]
        
        max_val = max(nums)
        if max_val < target:
            return len(nums)
        min_val = min(nums)
        if min_val > target:
            return 0

        
        

        