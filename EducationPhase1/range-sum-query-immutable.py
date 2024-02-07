class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]*len(nums)
        for i in range(len(nums)):
            self.pre[i] += self.pre[i-1] + nums[i]
        self.pre.append(0)
        print(self.pre)


    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right]-self.pre[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)