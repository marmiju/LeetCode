class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        none_zero_index = 0

        for i in range(len(nums)) :
            if nums[i] != 0:
                nums[none_zero_index] = nums[i]
                if none_zero_index != i:
                    nums[i] = 0
                none_zero_index += 1





        