from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        def steps_in_range(l: int, r: int) -> int:
            total_steps = 0
            base = 1      # starting of each step interval
            step = 1      # current step number
            while base <= r:
                left = base
                right = base * 4 - 1  # end of this interval
                # overlap with [l, r]
                start = max(l, left)
                end = min(r, right)
                if start <= end:
                    count = end - start + 1
                    total_steps += count * step
                base *= 4
                step += 1
            return total_steps

        total_result = 0
        for l, r in queries:
            total_steps = steps_in_range(l, r)
            # one operation reduces 2 steps → ceil
            total_result += (total_steps + 1) // 2

        return total_result
