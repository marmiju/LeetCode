from typing import List

class Solution:
    def searchValue(self, mat, tar, row) -> bool:
        m = len(mat[0])
        st = 0
        end = m - 1
        while st <= end:
            mid = st + (end - st) // 2
            if mat[row][mid] == tar:
                return True
            elif tar > mat[row][mid]:
                st = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat)      # number of rows
        m = len(mat[0])   # number of columns
        stRow = 0
        endRow = n - 1

        while stRow <= endRow:
            midRow = stRow + (endRow - stRow) // 2
            if mat[midRow][0] <= target <= mat[midRow][m - 1]:
                return self.searchValue(mat, target, midRow)
            elif target > mat[midRow][m - 1]:
                stRow = midRow + 1
            else:
                endRow = midRow - 1

        return False
