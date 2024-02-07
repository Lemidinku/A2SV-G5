class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0]*n
        freq = defaultdict(int)
        freq[0] = 1

        summ = 0
        count =0
        for num in nums:
            summ+=num
            count += freq[summ%k]
            freq[summ%k] += 1
        return count

