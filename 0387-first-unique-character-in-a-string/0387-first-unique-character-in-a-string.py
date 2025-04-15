class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i,val in enumerate(s):
            if count[val] == 1:
                return i
        
        return -1
        
        
        