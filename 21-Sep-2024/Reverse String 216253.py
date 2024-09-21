# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rev(s,left,right):
            if left>=right:
                return 
            s[left],s[right] = s[right],s[left]
            rev(s,left+1,right-1)

        rev(s, 0, len(s)-1)
