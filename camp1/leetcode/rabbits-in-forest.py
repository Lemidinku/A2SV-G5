class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()

        rabbits = 0
        curr =-1
        ofCurrColor =0

        for answer in answers:
            if answer != curr or not curr:  
                rabbits += answer+1
                curr = answer
                ofCurrColor = 0
            elif ofCurrColor == curr+1:
                rabbits += answer+1
                ofCurrColor = 0
            

            ofCurrColor +=1


        return rabbits