class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n//7
        summ = (full_weeks/2) * (7*full_weeks + 49)
        remaining = n%7
        summ += (remaining/2) *(2*(full_weeks+1)+remaining-1)
        return int(summ)