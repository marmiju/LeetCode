class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(ch.lower() for ch in s if ch.isalpha())
        return st == st[::-1]
        
        