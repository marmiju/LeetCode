class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = []

        for i in range(len(s)-1, -1,-1):
            result.append(s[i])
        
        return ' '.join(result)


        
        