class Solution:
    def maxScore(self, s: str) -> int:
        max_val =0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            max_val = max(max_val,score)
        
        return max_val
            

        