class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0
        for _ in range(32):
            # Shift result left to make space for the next bit
            result <<= 1
            # Add the last bit of n
            result |= (n & 1)
            # Shift n right to process the next bit
            n >>= 1
        return result

        