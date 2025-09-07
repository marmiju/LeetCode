class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        return " ".join(word[::-1])
        
        