class Solution:
    def average(self, salary: List[int]) -> float:
        tot = sum(salary)-max(salary)-min(salary)
        return tot / (len(salary)-2)