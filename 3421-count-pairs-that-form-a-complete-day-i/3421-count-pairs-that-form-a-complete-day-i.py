from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mod_count = defaultdict(int)
        count = 0

        for hour in hours:
            mod = hour % 24
            complement = (24 - mod) % 24  # to handle mod = 0 correctly
            count += mod_count[complement]
            mod_count[mod] += 1

        return count
