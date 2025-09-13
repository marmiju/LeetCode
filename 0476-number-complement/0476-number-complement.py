class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num)[2:])
        print(binary)
        left,right= 0, len(binary) -1
        for i, n in enumerate(binary):
            binary[i] = '0' if n == '1' else '1'
        
        return int("".join(binary),2)

        