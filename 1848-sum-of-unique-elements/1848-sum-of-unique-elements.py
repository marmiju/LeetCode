class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = 0

        for val, freq in count.items():
            if freq == 1:
                total += val
        return total
