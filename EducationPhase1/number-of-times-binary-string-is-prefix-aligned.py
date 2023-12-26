class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0
        count = 0
        for i in range(len(flips)):
            max_flip = max(flips[i],max_flip)

            if max_flip == i+1:
                count +=1
        return count