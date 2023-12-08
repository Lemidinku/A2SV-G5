class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_nums = []
        equals = []
        more_nums = []
        for num in nums:
            if num<pivot:
                less_nums.append(num)
            elif num==pivot:
                equals.append(num)
            else:
                more_nums.append(num)
        return less_nums+equals+more_nums
                