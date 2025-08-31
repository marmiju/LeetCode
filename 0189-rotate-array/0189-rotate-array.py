class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        l = len(nums)

        k = k%l

        left = nums[0:l-k]
        right = nums[l-k:]

        nums[:] = right + left

        
        return nums
        