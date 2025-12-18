class Solution:
    def srachValue(self, row, target):
        n = len(row)
        st = 0
        end = n-1

        while st <= end:
            mid = st + (end -st)//2
            if row[mid] < target:
                st = mid +1
            elif row[mid] > target :
                end = mid -1
            else:
                return True
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        st_row = 0
        end_row = row -1

        while st_row <= end_row:
            mid = st_row + (end_row-st_row)//2
            if matrix[mid][0] <= target <= matrix[mid][col-1]:
                return self.srachValue(matrix[mid], target)
            elif matrix[mid][0] > target:
                end_row = mid -1
            else:
                st_row = mid + 1
        return False
