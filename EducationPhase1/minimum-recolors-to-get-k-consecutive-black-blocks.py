class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        white = 0
        for i in range(k): 
            if blocks[i]=="W": white += 1
        min_white = white

        for right in range(k,len(blocks)):
            if blocks[right]=="W": white+=1
            if blocks[right-k]=="W": white-=1

            min_white = min(white,min_white)
        return min_white
            
            

