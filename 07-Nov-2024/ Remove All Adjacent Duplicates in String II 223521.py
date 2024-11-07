# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # (char, count)
        
        for char in s:

                if stack and stack[-1][0]==char and stack[-1][1]+1 == k:
                    stack.pop()
                elif stack and stack[-1][0]==char:
                    stack[-1][1] +=1
                else:
                    stack.append([char,1])

        result = ""
        for char,count in stack:
            result += char*count
    
        return result