class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] =0
        moves = 0
        for x in range(n):
            if nums[x] != 0:
                nums[moves] = nums[x]
                moves += 1
        
        for z in range(moves,n):
            nums[z] = 0
        
        return nums

        