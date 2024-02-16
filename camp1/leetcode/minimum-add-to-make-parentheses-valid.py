class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        moves = 0
        for i in range(len(s)):

            if s[i]=="(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    moves+=1

        moves += len(stack)

        return moves

