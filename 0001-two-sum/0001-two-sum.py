class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        disc = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in disc :
                return [disc[diff],i]
            disc[n] = i
        return
        