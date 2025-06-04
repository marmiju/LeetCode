class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op = 0
        for num in nums:
            if num < k:
                op += 1
        
        return op

        