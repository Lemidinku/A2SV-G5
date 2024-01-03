class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(reverse=True)
        s.sort(reverse=True)
        child, cookie = 0,0
        count = 0
        while child<len(g) and cookie<len(s):
            if g[child]<=s[cookie]:
                count +=1
                child+=1
                cookie+=1
            else:
                child+=1
        
        return count
        

