class Solution:
    def maxScore(self, s: str) -> int:
        
        tot_ones  = 0 
        for a in s:
            if a == "1": 
                tot_ones += 1 
        ones = 0
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == "1": 
                ones +=1
            # no_zeros to the left = (i+1-ones)
            # no_ones to the right = tot_ones-ones
            score = (i+1-ones) + (tot_ones-ones)
            max_score = max(max_score, score)
        return max_score


