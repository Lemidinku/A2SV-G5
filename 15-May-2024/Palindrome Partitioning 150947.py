# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def isPalindrome(word):
            i=0
            j = len(word)-1
            while i<j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True
        combs = []
        curr = []
        def backtrack(i):
            if i>=n-1:
                combs.append(curr[:])
                return 

            for j in range(i+1, n):
                if isPalindrome(s[i+1:j+1]):
                    curr.append(s[i+1:j+1])
                    backtrack(j)
                    curr.pop()
            return 
        backtrack(-1)
        return combs

