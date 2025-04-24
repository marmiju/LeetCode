class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        count_s = Counter(s)
        count_t = Counter(t)
        
       
        for char, cnt in count_t.items():
            if cnt > count_s[char]:
                return char
