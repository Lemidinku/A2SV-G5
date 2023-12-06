class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        new_arr =[]
        while left<n and right<2*n:
            new_arr.append(nums[left])
            new_arr.append(nums[right])
            left+=1
            right +=1
        return new_arr

