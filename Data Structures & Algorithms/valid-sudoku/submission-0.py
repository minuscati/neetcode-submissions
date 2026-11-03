class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            count_r = set()
            # row check
            for j in row:
                if j!=".":
                    if j in count_r:
                        return False
                    else:
                        count_r.add(j)
        # column check
        for k in range(9):
            count_c = set()
            column = [row[k] for row in board]
            for s in column:
                if s!=".":
                    if s in count_c:
                        return False
                    else:
                        count_c.add(s)
        # 3x3check
        for i in range(0,9,3):
            for j in range(0,9,3):
                count_s = set()

                for r in range(i,i+3):
                    for c in range(j,j+3):
                        num = board[r][c]

                        if num!=".":
                            if num in count_s:
                                return False
                            else:
                                count_s.add(num) 
        return True