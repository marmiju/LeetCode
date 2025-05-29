class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        allsum = sum(nums)
        elsum = 0

        for num in nums:
            for digit in str(num):
                elsum += int(digit)
            
        
        return allsum - elsum

        