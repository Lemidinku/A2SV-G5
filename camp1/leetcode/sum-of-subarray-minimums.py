class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        ans = 0
        for ind,num in enumerate(arr):
            while stack and stack[-1][1] > num:
                prev_ind, prev_num = stack.pop()

                left = prev_ind-stack[-1][0] if stack else prev_ind+1
                right = ind-prev_ind

                subarrays = left*right
                ans += prev_num*subarrays
            stack.append((ind,num))


        for i in range(len(stack)):
            ind, num = stack[i]
            left = ind-stack[i-1][0] if i > 0 else ind+1
            right = n- ind

            subarrays = left*right
            ans += num *subarrays


        return ans% (10**9+7)


                