class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n =len(nums)
        count =0
        summ = 0
        freq = defaultdict(int)
        freq[0] = 1
        
        for num in nums:
            summ += num
            count += freq[summ-k]
            freq[summ] += 1
        return count


            





    