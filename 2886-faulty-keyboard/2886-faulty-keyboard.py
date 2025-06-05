class Solution:
    def reverse(self, char:list):
        left, right = 0,len(char)-1
        while left < right:
            char[left], char[right] = char[right],char[left]
            left += 1
            right -= 1
        return char

    def finalString(self, s: str) -> str:
        s= list(s)
        result = []
        for i in range(len(s)):
            if s[i] == 'i':
               result = self.reverse(result)
            else:
                result.append(s[i])
        return ''.join(result)


        