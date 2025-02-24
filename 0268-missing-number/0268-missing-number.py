class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum =  n* (n+1)//2
        total = 0
        for num in nums:
            total += num
        
        return expected_sum - total

        
        