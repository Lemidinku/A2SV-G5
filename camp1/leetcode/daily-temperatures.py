class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0]*n
        mono_stack = []

        for i in range(n):
            while mono_stack and temps[mono_stack[-1]]< temps[i]:
                res[mono_stack[-1]] = i-mono_stack[-1]
                mono_stack.pop()
            mono_stack.append(i)


        return res