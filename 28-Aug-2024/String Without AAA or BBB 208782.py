# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            rem = a-b
            s = ""
            for i in range(b):
                if rem:
                    s += "a"
                    rem -=1
                s+="a"
                s+="b"
            s += "a"*(rem)
            return s
        else:
            rem = b-a
            s = ""
            for i in range(a):
                if rem:
                    s += "b"
                    rem -=1
                s+="b"
                s+="a"
            s += "b"*(rem)

            return s