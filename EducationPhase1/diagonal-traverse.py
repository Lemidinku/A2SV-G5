class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def inbound(x,y):
            return 0<=x<m and 0<=y<n
        m, n = len(mat), len(mat[0])
        traversal = []
        dir = (-1,1)
        row, col = 0, 0

        for _ in range(n*m):
            
            traversal.append(mat[row][col])
            if dir == (-1,1):
                x,y = row+dir[0], col+dir[1]
                if inbound(x,y):
                    row,col = x,y
                elif inbound(row, col+1):
                    col += 1
                    dir = (1,-1)

                else:
                    row += 1
                    dir = (1,-1)
                    
            else:
                x,y = row+dir[0], col+dir[1]
                if inbound(x,y):
                    row,col = x,y
                elif inbound(row+1, col):
                    row += 1
                    dir = (-1,1)
                else:
                    col += 1
                    dir = (-1,1)
        return traversal