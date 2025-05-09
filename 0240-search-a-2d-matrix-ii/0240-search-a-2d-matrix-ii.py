class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat) 
        n = len(mat[0])
        r = 0
        c= n -1

        while(r < m and c >= 0):
            if mat[r][c] == target:
                return True
            elif target < mat[r][c]:
                c -= 1
            else:
                r += 1
        
        return False