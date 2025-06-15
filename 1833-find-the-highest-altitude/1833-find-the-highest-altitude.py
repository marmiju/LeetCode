class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_val = 0
        c_val = 0
        for g in gain:
            c_val += g
            max_val = max(max_val,c_val)
        
        return max_val