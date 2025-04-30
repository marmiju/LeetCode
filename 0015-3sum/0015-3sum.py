from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # Sort the array first

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            j, k = i + 1, len(nums) - 1

            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum < 0:
                    j += 1
                elif _sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
