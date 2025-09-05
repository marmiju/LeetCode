class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        start = 1
        if n <= 2:
            return n

        for i in range(2,n):
            if nums[i] != nums[start -1]:
                start += 1
                nums[start] = nums[i]
           
        
        return start+1


        