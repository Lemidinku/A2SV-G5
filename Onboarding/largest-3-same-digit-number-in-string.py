class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        max_good = ""
        max_digit = float('-infinity')

        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2] and int(num[i]) > max_digit:
                max_good = num[i:i+3]
                max_digit = int(num[i])
        return max_good