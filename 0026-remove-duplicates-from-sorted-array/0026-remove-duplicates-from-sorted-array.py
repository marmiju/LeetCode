class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                ans += 1
                nums[ans] = nums[i]
        
        return ans+1
        