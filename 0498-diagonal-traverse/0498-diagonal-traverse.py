class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        # There are m + n - 1 diagonals total
        for d in range(m + n - 1):
            temp = []
            
            # figure out the starting row & column
            if d < n:
                r, c = 0, d
            else:
                r, c = d - n + 1, n - 1
            
            # collect elements along the diagonal
            while r < m and c >= 0:
                temp.append(mat[r][c])
                r += 1
                c -= 1
            
            # reverse on even diagonals
            if d % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
        
        return result
        