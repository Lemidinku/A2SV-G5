# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        self.filled = 0

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] !=".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i//3,j//3)].add(board[i][j])
                    self.filled +=1

        def canPlace(val, r, c):
            val = str(val)
            if val in rows[r]: return False
            if val in cols[c]: return False
            if val in squares[(r//3,c//3)]: return False
            return True
        def place_number(val,r,c):
            val = str(val)
            rows[r].add(val)
            cols[c].add(val)
            squares[(r//3,c//3)].add(val)
            self.filled +=1
        def remove_number(val,r,c):
            val = str(val)
            rows[r].remove(val)
            cols[c].remove(val)
            squares[(r//3,c//3)].remove(val)
            self.filled -=1

        
        ans = []
        
        def backtrack(row,col):

            if self.filled == (len(board)*len(board)):
                return True

            if board[row][col] !="." :
                c = (col+1)%len(board)
                r = row+1 if col+1==len(board) else row
                if backtrack(r,c): return True
                return 

            for num in range(1, 10):
                if canPlace(num,row, col):
                    place_number(num,row, col)
                    board[row][col] = str(num)
                    c = (col+1)%len(board)
                    r = row+1 if col+1==len(board) else row
                    if backtrack(r,c): return True
                    remove_number(num,row, col)
                    board[row][col] = "."

        backtrack(0,0)









        