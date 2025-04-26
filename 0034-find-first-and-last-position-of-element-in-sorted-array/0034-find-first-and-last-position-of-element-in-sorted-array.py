class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i, val in enumerate(nums):
            if val == target:
                result.append(i)
        
        if not result:
            return [-1,-1]
        
        min_res = min(result)
        max_res = max(result)

        return [min_res, max_res]


        