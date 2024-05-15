# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindromes = set()
        def isPalindrome(word):
            if word in palindromes:
                return True
            i=0
            j = len(word)-1

            while i<j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            palindromes.add(word)
            return True
        dp = [-1]*n
        def backtrack(i):
            if i>=n:
                return 0
            if dp[i] == -1:
                cuts = float('inf')
                for j in range(i, n):
                    if isPalindrome(s[i:j+1]):
                        cuts = min(backtrack(j+1),cuts)
                dp[i] = cuts +1
            return dp[i]
        
        return backtrack(0)-1