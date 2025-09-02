from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by x ascending, and for same x sort by y descending
        points.sort(key=lambda p: (p[0], -p[1]))

        n = len(points)
        ans = 0

        for i in range(n):
            _, yi = points[i]
            maxY = -10**9  # something smaller than any y in input
            # scan points to the right (including those with same x but smaller y)
            for j in range(i+1, n):
                _, yj = points[j]
                # condition: yi >= yj AND yj is strictly greater than any previously
                # counted y (so no other point lies on/in the rectangle/line)
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj
        return ans




        