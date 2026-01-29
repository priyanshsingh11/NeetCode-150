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
