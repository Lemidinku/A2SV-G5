# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        dp = [0]*(n)
        for i in reversed(range(n)):
            prev_ind = i+ questions[i][1]+1

            dp[i]  = questions[i][0]
            if prev_ind < n:
                dp[i] += dp[prev_ind]
            if i<n-1:
                dp[i] = max(dp[i], dp[i+1])
        return max(dp)

            