class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        size = len(nums)
        if size % 2 != 0:
            return False
        count =Counter(nums)
        for val in count.values():
           if val > 2:
            return False
        
        return True


        