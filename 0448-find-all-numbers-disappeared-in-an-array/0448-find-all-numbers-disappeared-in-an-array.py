class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full_set = set(range(1,n+1))
        nums_set = set(nums)
        return list(full_set - nums_set)

        