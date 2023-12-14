class FrequencyTracker:

    def __init__(self):
        self.fre = defaultdict(int)
        self.fre_fre = defaultdict(int)

    def add(self, number: int) -> None:
        self.fre_fre[self.fre[number]] -= 1
        self.fre[number] += 1
        self.fre_fre[self.fre[number]] +=1

    def deleteOne(self, number: int) -> None:
        if self.fre[number] > 0:
            self.fre_fre[self.fre[number]] -= 1
            self.fre[number] -= 1
            self.fre_fre[self.fre[number]] +=1
            
    def hasFrequency(self, frequency: int) -> bool:
        return self.fre_fre[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)