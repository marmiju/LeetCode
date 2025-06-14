class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        left = 0
        window_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # Slide window until unique
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            window_sum += nums[right]

            # If window size == k
            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

                # Slide window forward
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

        return max_sum
