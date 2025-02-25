class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        exist ={}
        for char in s:
            exist[char] = exist.get(char,0) + 1
        
        freq_values = set(exist.values())

        if len(freq_values) == 1:
            return True
        else:
            return False
