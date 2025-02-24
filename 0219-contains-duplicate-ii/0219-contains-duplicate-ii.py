class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        exist = {}

        for i,num in enumerate(nums):
            if num in exist and i - exist[num] <= k:
                return True
                
                
            exist[num] = i
        return False

        