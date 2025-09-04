class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        dx = abs(x-z)
        dy = abs(y-z)

        if dx < dy:return 1
        elif dx > dy: return 2
        else: return 0 