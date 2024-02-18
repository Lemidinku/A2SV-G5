class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in "{([":
                stack.append(char)
            else:
                if stack and stack[-1]== opening[char]:
                    stack.pop()
                else:
                    return False

        if stack: return False
        return True



