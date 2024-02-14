class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.tens = self.fives = 0
        def returnChange(amount):
            if amount==15:
                if self.tens:
                    self.tens-=1
                    self.fives-=1
                else:
                    self.fives-=3
            elif amount==5:
                self.fives-=1

        
        for bill in bills:
            print(bill, self.fives, self.tens)
            change = bill-5
            changeReturn15 = (self.tens and self.fives) or (self.fives>2)
            if change==15 and (changeReturn15):
                returnChange(15)
            elif change==5 and (change<=(self.fives*5)):
                returnChange(5)
            elif change: 
                return False





            if bill==5: self.fives+=1
            if bill==10: self.tens+=1
        return True

                
            

            
            
