class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            rem = target - nums[i]
            if rem in seen:
                return [seen[rem],i]
            else:
                seen[nums[i]] = i
        
        