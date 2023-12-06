class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numb1 ,numb2 = 0, 0
        
        #change the first number 
        for i in range(len(num1)):
            j = -1
            while str(j) != num1[i]:
                j += 1
            multi = 10**(len(num1)-i-1)
            numb1 += j*(multi)

        #change the second number 
        for i in range(len(num2)):
            j = -1
            while str(j) != num2[i]:
                j += 1
            multi = 10**(len(num2)-i-1)
            numb2 += j*(multi)
        
        return str(numb1*numb2)

