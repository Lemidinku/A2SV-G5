class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digit = digits[i] + carry
            if digit == 10:
                result.append(0)
            else:
                carry = 0
                result.append(digit)
            
        if carry: result.append(1)
        return result[::-1]