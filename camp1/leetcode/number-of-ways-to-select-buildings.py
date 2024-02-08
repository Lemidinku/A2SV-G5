class Solution:
    def numberOfWays(self, s: str) -> int:
        tot_zeros = 0
        tot_ones = 0

        for building in s:
            if building=="1":
                tot_ones+=1
            else: tot_zeros+=1

        
        ones = 0
        zeros = 0
        count = 0
        for building in s:
            if building=="1":
                count += (zeros*(tot_zeros-zeros))
                ones += 1
            else:
                count += (ones*(tot_ones-ones))
                zeros +=1
        
        return count