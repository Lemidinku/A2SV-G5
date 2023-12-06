class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        majorities = []
        for num in freq.keys():
            if freq[num] > (n//3):
                majorities.append(num)

        return majorities