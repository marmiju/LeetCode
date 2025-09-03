import math

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        ans = 0

        # Sort by x ascending, y descending
        points.sort(key=lambda p: (p[0], -p[1]))

        for i, (_, yi) in enumerate(points):
            maxY = -math.inf
            # Attempt each point to the right (or same x, lower y)
            for j in range(i + 1, len(points)):
                _, yj = points[j]
                # Valid if yj is below or equal to yi, and above previous maxY
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj

        return ans
