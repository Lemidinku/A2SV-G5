class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix[0])
        m = len(matrix)
        pre = [[0]*(n+1) for _ in range(m+1)]

        for r in range(1,m+1):
            
            for c in range(1,n+1):
                pre[r][c] += pre[r][c-1] + matrix[r-1][c-1]

        count = 0
        for left in range(n):
            for right in range(left+1, n+1):
                freq = defaultdict(int)
                summ = 0
                for row in range(m+1):
                    summ += (pre[row][right]-pre[row][left])
                    count += freq[summ-target] 
                    freq[summ] += 1

        return count
        




    
 



                
        
