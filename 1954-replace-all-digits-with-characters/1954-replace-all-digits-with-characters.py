class Solution:
    def replaceDigits(self, s: str) -> str:
        result  = list(s)

        for i in range(1,len(s),2):
            befor_char = s[i-1]
            digit  = int(s[i])
            result[i] = chr(ord(befor_char) + digit)
        
        return "".join(result)
        