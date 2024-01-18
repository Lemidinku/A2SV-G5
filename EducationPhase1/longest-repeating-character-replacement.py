class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        window = {}
        res = 0
        left =0
        for right in range(n):
            if s[right] in window: window[s[right]]+=1
            else: window[s[right]]=1

            while right-left+1-max(window.values())>k:
                window[s[left]]-=1
                left+=1
            res = max(res,right-left+1)
        return res