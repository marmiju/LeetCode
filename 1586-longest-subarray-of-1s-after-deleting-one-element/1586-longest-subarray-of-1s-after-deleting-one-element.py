class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            
            while(count > 1):
                if nums[left] == 0:
                    count -= 1
                
                left += 1
            
            ans = max(ans,right -left)
        return ans