class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums)%p
        if not rem: return 0

        pre = [0]*len(nums)
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]
            pre[i]+=summ
        
        pre.insert(0,0)
        print(pre,rem)

        freq = {}
        freq[0] = 0
        min_len = float("inf")
        for i in range(len(pre)):
            if (pre[i]-rem)%p in freq:
                min_len = min(min_len, i-freq[(pre[i]-rem)%p])
            freq[pre[i]%p] = i
        

        
        return min_len if min_len<len(nums) else -1

        # [0, 3, 4, 8, 10]

        