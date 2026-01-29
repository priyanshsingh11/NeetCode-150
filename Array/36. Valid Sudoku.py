class Solution(object):
    def isValidSudoku(self, board):
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes={}

        for r in range(9):
            for c in range(9):
                val=board[r][c]

                if val=='.':
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                if val in cols[c]:
                    return False
                cols[c].add(val)

                
                box=(r//3,c//3)
                if box not in boxes:
                    boxes[box]=set()

                if val in boxes[box]:
                    return False
                boxes[box].add(val)

        return True

# -------- 3x3 BOX LOGIC (IMPORTANT) --------
# Each 3x3 box is identified using (row // 3, col // 3)
# All cells that give the same (row//3, col//3) belong to the SAME box
#
# boxes is a dictionary:
#   key   -> (box_row, box_col)
#   value -> set of numbers already seen in that box
#
# Steps:
# 1. Find which box the current cell belongs to
# 2. If this box is visited for the first time, create an empty set for it
# 3. If the value already exists in the box set -> Sudoku is INVALID
# 4. Otherwise, add the value to the box set
#
# Example:
# Cell (4,7) -> (4//3, 7//3) -> (1,2) -> middle-right box
# ------------------------------------------
