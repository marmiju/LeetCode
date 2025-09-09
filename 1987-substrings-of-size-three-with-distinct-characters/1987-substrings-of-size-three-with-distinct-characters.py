class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(2,n):
            if s[i] != s[i-1] and s[i] != s[i-2] and s[i-1] != s[i-2]:
                ans += 1
        return ans
        