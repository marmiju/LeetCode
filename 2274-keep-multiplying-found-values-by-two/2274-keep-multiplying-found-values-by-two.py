class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        org = original
        while True:
            if org in nums:
                org *= 2
            else:
                return org


        