class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec = int(a,2) + int(b,2)
        return bin(dec)[2:]
        