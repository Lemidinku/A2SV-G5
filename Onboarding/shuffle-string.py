class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result =["_" for _ in range(len(s))]
        for char,ind in zip(s,indices):
            result[ind] = char
        return "".join(result)