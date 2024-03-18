class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbid = set(forbidden)
        n = len(word)
        word = list(word)
        def hasForbidden(st):
            s = window[-10:]
            for i in range(len(s)):
                if s[i:] in forbid:
                    return True
            return False
                    
        left = 0
        max_len = 0
        window = ""
        for right in range(n):
            window += word[right]

            while window and hasForbidden(window):
                window = window[1:]
            max_len = max(max_len, len(window))

        return max_len
                
                

