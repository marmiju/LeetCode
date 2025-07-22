from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]):
        count = Counter(nums)
        
        max_len = 0
        
        for num in count:
            if num + 1 in count:
                max_len= max(max_len, count[num] + count [num + 1])
            
        
        return max_len