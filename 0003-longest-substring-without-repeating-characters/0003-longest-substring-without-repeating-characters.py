class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        lngs = set()
        max_len = 0
        left = 0

        for right in range(n):
            while s[right] in lngs:
                lngs.remove(s[left])
                left+=1
            lngs.add(s[right])
            max_len =max(max_len, right -left +1)

        return max_len
