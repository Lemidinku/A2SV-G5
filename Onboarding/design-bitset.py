class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = [0]*size
        self.rev_bitset = [1]*size
        self.flips = 0
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.flips%2:
            if self.bitset[idx]:
                self.ones -= 1
            self.bitset[idx] = 0
            self.rev_bitset[idx] = 1
        else:
            if not self.bitset[idx]:
                self.ones += 1
            self.bitset[idx] = 1
            self.rev_bitset[idx] = 0
        
    def unfix(self, idx: int) -> None:
        if self.flips%2:
            if not self.bitset[idx]:
                self.ones += 1
            self.bitset[idx] = 1
            self.rev_bitset[idx] = 0
        else:
            if self.bitset[idx]:
                self.ones -= 1
            self.bitset[idx] = 0
            self.rev_bitset[idx] = 1

    def flip(self) -> None:
        self.flips += 1


    def all(self) -> bool:
        if self.flips%2:
            return self.ones == 0
        
        return self.ones == self.size

    def one(self) -> bool:
        if self.flips%2:
            return self.ones < self.size
        return self.ones > 0

    def count(self) -> int:
        if self.flips%2:
            return  self.size - self.ones
        return self.ones

    def toString(self) -> str:
        if self.flips%2:
            return "".join(map(str,self.rev_bitset))
        return "".join(map(str,self.bitset))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()