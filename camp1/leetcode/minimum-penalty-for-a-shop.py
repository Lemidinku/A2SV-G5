class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        tot_cos = 0
        for a in customers:
            if a =="Y":
                tot_cos +=1

        yeses = 0
        min_penality = float("inf")
        earilest = 0
        for i in range(len(customers)):
            penality = tot_cos-yeses + (i-yeses)
            if min_penality> penality:
                min_penality = penality
                earilest = i
            if customers[i]=="Y":
                yeses +=1
        if min_penality> len(customers)-tot_cos:
            min_penality = len(customers)-tot_cos
            earilest = len(customers)
        
        return earilest

            


