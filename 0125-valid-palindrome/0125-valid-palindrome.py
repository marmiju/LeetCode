class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "".join([char.upper() for char in s if char.isalnum()])
        second = alphabet[::-1]

        return alphabet == second
        