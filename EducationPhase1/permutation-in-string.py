from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        word1 = Counter(s1)
        subarray = {}
        for r in range(len(s2)):
            if s2[r] in word1:
                if s2[r] in subarray: subarray[s2[r]]+=1
                else: subarray[s2[r]]=1

                while subarray[s2[r]]>word1[s2[r]]:
                    subarray[s2[l]]-=1
                    l+=1

            else:
                l=r+1
                subarray = {}
            if subarray==word1:return True
        return False

            