class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n-1

        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start +=1
            else:
                return [start+1, end+1]  

        