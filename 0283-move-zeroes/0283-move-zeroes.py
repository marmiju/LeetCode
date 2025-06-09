class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moves = 0
        for i,num in enumerate(nums):
            if num != 0:
                nums[moves] = num
                moves += 1
        
        for i in range(moves,len(nums)):
            nums[i] = 0
        
        return nums
        