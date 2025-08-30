class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # check row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # check column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # check 3x3 box
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        
        return True
