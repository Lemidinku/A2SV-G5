class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        s = ["("]
        def backtrack(opening,closing):
            if len(s)==2*n:
                result.append("".join(s))
                return 
            if opening:
                s.append("(")
                backtrack(opening-1,closing)
                s.pop()
            if closing>opening:
                s.append(")")
                backtrack( opening,closing-1)
                s.pop()
        backtrack(n-1,n)
        return result