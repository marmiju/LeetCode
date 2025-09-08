class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n-1

        while start < end:
            _sum = nums[start] + nums[end]
            if _sum == target:
                return [start+1,end+1] 
            elif  _sum > target:
                end -= 1
            else:
                start +=1
             

        