class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)  # Convert the number to a string
        s2 = s1[::-1]  # Reverse the string
        
        return s1 == s2  # Check if the original and reversed strings are equal
