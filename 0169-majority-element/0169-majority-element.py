class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = set(nums)

        for val in major:
            if nums.count(val) > len(nums)//2:
                return val
        
        