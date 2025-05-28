class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        arr =sorted(nums)
        op1 = arr[-1] * arr[-2]* arr[-3]
        op2 = arr[0]*arr[1]*arr[-1]
        return max(op1,op2)



       
        