class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.cols, self.rows = len(board[0]), len(board)
        visited = set()
        curr_word = []
        def dfs(row, col):
            if len(curr_word)==len(word):
                return True

            if word[len(curr_word)] != board[row][col]: return 
            if (row,col) in visited: return
            
            visited.add((row, col))
            curr_word.append(board[row][col])
            
            for x,y in [(1,0), (0,1),(-1,0), (0,-1)]:
                if 0<=row+x<self.rows and 0<=col+y<self.cols:
                    if dfs(row+x, col+y): return True
            curr_word.pop()
            visited.remove((row, col))
            return False
        
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word: return True
                if board[i][j] != word[0]: continue
                if dfs(i,j): return True

        return False




        