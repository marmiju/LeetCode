class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        c_num = [num for num in nums if num >= k]
        return len(nums) - len(c_num)

        