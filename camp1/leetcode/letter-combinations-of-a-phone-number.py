class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys ={"2":"abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9":"wyxz"}
        if not len(digits): return []
        
        lis = [x for x in keys[digits[0]]]
        i=1
        while i<len(digits):
            new_lis = []
            for letters in lis:
                new_lis += [letters+x for x in keys[digits[i]]]
            lis = new_lis
            i+=1
        return lis