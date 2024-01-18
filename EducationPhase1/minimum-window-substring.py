class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n,m = len(s), len(t)
        min_len = float('inf')
        word = Counter(t)
        window = Counter("")
        left=0
        start,end = 0,0
        for right in range(n):
            window[s[right]] += 1

            while window >= word:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    start,end = left, right
                window[s[left]] -= 1
                left +=1
        
        if min_len > n: return ""
        return s[start:end+1]
                
            

       