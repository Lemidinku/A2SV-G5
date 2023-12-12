class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        twenty_5 = len(arr)*(0.25)
        count = Counter(arr)
        for num,fre in count.items():
            if fre > twenty_5:
                return num