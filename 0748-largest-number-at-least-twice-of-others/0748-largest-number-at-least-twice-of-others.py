class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_index = nums.index(max_val)

        for i, num in enumerate(nums):
            if num * 2 > max_val and max_index != i:
                return -1

        return max_index 

        