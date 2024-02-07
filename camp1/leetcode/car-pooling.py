class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for _,_,to in trips:
            n = max(n, to)
        
        pre = [0]*(n+1)

        for peoples, fromm ,to in trips:
            
            pre[fromm] +=peoples
            pre[to] -= peoples

        summ = 0
        for num in pre:
            summ+=num
            if summ>capacity: return False

        return True

