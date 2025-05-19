class Solution:
    def replaceDigits(self, s: str) -> str:
        result  = list(s)

        for i in range(1,len(s),2):
            digit  = int(s[i])
            result[i] = chr(ord(s[i-1]) + digit)
        
        return "".join(result)
        