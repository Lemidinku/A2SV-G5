class ATM:

    def __init__(self):
        self.notes = defaultdict(int)
        

    def deposit(self, banknotesCount: List[int]) -> None:
        bills = [20, 50, 100, 200, 500]
        for i in range(len(bills)):
            self.notes[bills[i]]+= banknotesCount[i]
           
        

    def withdraw(self, amount: int) -> List[int]:
        print(self.notes, amount)
        bills = [500, 200, 100, 50, 20]
        result = [0]*5
        i = 0
        while amount and i<len(bills):
            if amount >= bills[i]:
                amount_with_this_bill = amount//bills[i]
                bill_given = min(amount_with_this_bill,self.notes[bills[i]])
                result[i] = bill_given
                amount -= bill_given*bills[i]
                print(bill_given,amount)

            i+=1
        if not amount:
            for i in range(len(result)):
                self.notes[bills[i]]-=result[i]
        return [-1] if amount else result[::-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)