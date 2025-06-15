class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            current_sum += num
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1

        return count
