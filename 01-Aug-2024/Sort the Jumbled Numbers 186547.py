# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def mappedValue(num):
            val = ''
            for digit in str(num):
                val += str(mapping[int(digit)])
            return int(val)

        nums.sort(key= lambda x:mappedValue(x))
        return nums
