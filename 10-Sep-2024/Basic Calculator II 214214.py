# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)+1
        stack = [0]
        s = "+"+s
        i =0
        while i<n:
            op = s[i]
            num = ""
            i+=1
            while i<n and s[i] not in ["+", "-", "*", "/"]:
                if s[i] !=" ": num += s[i]
                i+=1
            if op=="/":
                last_op, last_num = stack.pop()
                stack.append((last_op, last_num//int(num)))
            elif op=="*":
                last_op, last_num = stack.pop()
                stack.append((last_op, last_num*int(num)))
            else:
                stack.append((op,int(num)))  

        ans  = 0
        for i in range(1, len(stack)):
            curr_op, curr_num = stack[i]
            if curr_op=="+":
                ans += curr_num
            else: ans -= curr_num

        # 1 + 10/3 + 1*2
        # 1 + 3 + 

        return ans
