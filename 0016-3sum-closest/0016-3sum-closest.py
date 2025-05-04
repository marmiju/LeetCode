class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')  # Initialize with infinity

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # If exact match found
                if curr_sum == target:
                    return curr_sum

                # Update the closest sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                # Move pointers based on comparison
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
