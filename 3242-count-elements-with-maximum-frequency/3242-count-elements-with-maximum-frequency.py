class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        max_freq = 0
        for val, freq in count.items():
           max_freq = max(max_freq, freq)
        
        for val, freq in count.items():
            if freq == max_freq:
                ans += freq
        return ans
