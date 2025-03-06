class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        exist ={}
        for char in s:
            if char in exist:
                exist[char] += 1
            else:
                exist[char] = 0
        freq = set(exist.values())
        return len(freq) == 1
        