class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n% 2 != 0 or n < 1 :
            return False

        return self.isPowerOfTwo(n//2)