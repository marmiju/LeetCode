class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # pre-size with -1 defaults
        
        for i in range(n):
            # look for the next greater by scanning forward (with wrap)
            for j in range(1, n):
                nxt = nums[(i + j) % n]
                if nxt > nums[i]:
                    result[i] = nxt
                    break
        
        return result



        