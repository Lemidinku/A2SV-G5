class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n,m = len(name), len(typed)
        top = 0
        bottom = 0

        if name[0]!= typed[0]:
            return False

        while top < n and bottom < m:
            if name[top] == typed[bottom]:
                top += 1
            elif bottom and typed[bottom] != typed[bottom-1]:
                return False
            bottom +=1

        
        while bottom < m:
            if typed[bottom] != name[-1]:
                return False
            bottom +=1

        return top == n