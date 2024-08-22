# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n,m = len(board),len(board[0])
        dir = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        def inbound(r,c):
            return ((0<=r<n) and (0<=c<m))
    
    
        def count_adjacent_mines(r,c):
            mines = 0
            for x,y in dir:
                if inbound(r+x,c+y) and board[r+x][c+y]=="M":
                    mines+=1
            return mines

        def click_(r,c):
            if board[r][c]=="M":
                board[r][c]="X"
                return 
            adjacent_mines = count_adjacent_mines(r,c)
            if adjacent_mines:
                board[r][c]=str(adjacent_mines)
                return 
            board[r][c]="B"
            for x,y in dir:
                if inbound(r+x,c+y) and board[r+x][c+y]=="E":
                    click_(r+x,c+y)
        
        row,col = click
        click_(row,col)

        return board

        
            