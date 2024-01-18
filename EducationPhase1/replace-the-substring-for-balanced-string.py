class Solution:
    def balancedString(self, s: str) -> int:
        def gt(dict1, dict2):
            return dict1["Q"] >= dict2["Q"] and dict1["W"] >= dict2["W"] and dict1["R"] >= dict2["R"] and dict1["E"] >= dict2["E"]


        n = len(s)
        count = Counter(s)
        to_be_replaced  = defaultdict(int)
        for a,b in count.items():
            if b > n//4:
                to_be_replaced[a] = b-n//4

        if not to_be_replaced: return 0
        window = defaultdict(int)
        min_len = n
        left = 0
        for right in range(n):
            window[s[right]] +=1

            while gt(window, to_be_replaced):
                min_len = min(min_len, right-left+1)
                window[s[left]] -=1
                left +=1
        return min_len



