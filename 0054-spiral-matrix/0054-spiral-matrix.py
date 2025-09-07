class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        count = 0
        total = n * m
        
        strow, endrow = 0, n - 1
        stcol, endcol = 0, m - 1
        ans = []

        while count < total:
            # left -> right
            for i in range(stcol, endcol + 1):
                if count < total:
                    ans.append(matrix[strow][i])
                    count += 1
            strow += 1

            # top -> bottom
            for i in range(strow, endrow + 1):
                if count < total:
                    ans.append(matrix[i][endcol])
                    count += 1
            endcol -= 1

            # right -> left
            for i in range(endcol, stcol - 1, -1):
                if count < total:
                    ans.append(matrix[endrow][i])
                    count += 1
            endrow -= 1

            # bottom -> top
            for i in range(endrow, strow - 1, -1):
                if count < total:
                    ans.append(matrix[i][stcol])
                    count += 1
            stcol += 1

        return ans
