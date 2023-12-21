class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            already_exist = set()
            for num in row:
                if num in already_exist:
                    return False
                if num!=".":
                    already_exist.add(num)

        for col in zip(*board):
            already_exist = set()
            for num in col:
                if num in already_exist:
                    return False
                if num!=".":
                    already_exist.add(num)

        
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]!="." and  board[r][c] in squares[(r//3,c//3)]:
                        return False 
                squares[(r//3,c//3)].add(board[r][c])
        return True