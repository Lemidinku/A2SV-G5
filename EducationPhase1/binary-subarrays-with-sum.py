class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        pref = [0]*n
        summ = 0
        for i in range(n):
            summ += nums[i]
            pref[i] = summ


        pref.insert(0,0) # I could've handled this in the above loop

        table = defaultdict(int)
        count = 0
        for num in pref:
            count += table[num]
            table[num+goal] += 1
        
        return count

