class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        anagrams = []
        count_p = Counter(p)
        count_s = Counter(s[:m])
        if count_p==count_s: anagrams.append(0)
        for i in range(m,n):
            count_s[s[i-m]] -= 1
            count_s[s[i]] += 1

            if count_p == count_s:
                anagrams.append(i-m+1)
            

        return anagrams

                




