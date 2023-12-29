class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [["."] * n for _ in range(m)]

        for x,y in walls:
            mat[x][y] = "w"
        for x,y in guards:
            mat[x][y] = "g"

        def mark_guarded_cells(mat,r,c):
            #upwards
            for row in range(r-1,-1,-1):
                if mat[row][c]== "w" or  mat[row][c]== "g":
                    break
                mat[row][c]= "1"

            #downwards
            for row in range(r+1,m):
                if mat[row][c]== "w" or  mat[row][c]== "g":
                    break
                mat[row][c]= "1"

            #to left
            for col in range(c-1,-1,-1):
                if mat[r][col]== "w" or  mat[r][col]== "g":
                    break
                mat[r][col]= "1"

            #to right
            for col in range(c+1,n):
                if mat[r][col]== "w" or  mat[r][col]== "g":
                    break
                mat[r][col]= "1"


                
        for x,y in guards:
            mark_guarded_cells(mat,x,y)


        unguarded = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==".":
                    unguarded+=1
        return unguarded





        

        