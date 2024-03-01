class Solution:
    def totalNQueens(self, n: int) -> int:
        attacked_cols = set()
        attacked_diagonals1 = set()
        attacked_diagonals2 = set()
        boards = []
        curr_board = [["."]*n for _ in range(n)]

        def valid(r,c):
            if c in attacked_cols: return False
            if r-c in attacked_diagonals1: return False
            if r+c in attacked_diagonals2: return False
            return True
        def removeQueen(r,c):
            attacked_cols.remove(c)
            attacked_diagonals1.remove(r-c)
            attacked_diagonals2.remove(r+c)
            curr_board[r][c] = "."
        def placeQueen(r,c):
            attacked_cols.add(c)
            attacked_diagonals1.add(r-c)
            attacked_diagonals2.add(r+c)
            curr_board[r][c] = "Q"


        def backtrack(i):
            if i==n:
                a = ["".join(row) for row in curr_board ]
                if a not in boards:
                    boards.append(a)
                return
            for col in range(n):
                if valid(i,col):
                    placeQueen(i,col)
                    backtrack(i+1)
                    removeQueen(i,col)
        backtrack(0)
        return len(boards)