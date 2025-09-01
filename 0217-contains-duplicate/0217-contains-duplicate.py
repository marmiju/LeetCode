class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        table = {}

        for val in nums:
            if val in table:
                return True
            table[val] = 1
        
        return False

        