# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        comb = []
        alpha_indices = [i for i in range(len(s)) if not s[i].isnumeric()]

        n = len(alpha_indices)
        for num in range(2**n):
            arr = list(s)

            for i in range(n):
                if num&(1<<i)==0:
                    arr[alpha_indices[i]] = arr[alpha_indices[i]].upper()
                else:
                    arr[alpha_indices[i]] = arr[alpha_indices[i]].lower()
            comb.append("".join(arr))


        return comb



















        # comb = []
        # def backtrack(i,curr):
        #     if i==len(s):
        #         comb.append(curr)
        #         return
            
        #     if s[i].isnumeric():
        #         backtrack(i+1,curr + s[i] )
        #     else:

        #         backtrack(i+1,curr + s[i].upper() )
        #         backtrack(i+1,curr + s[i].lower())
        
        # backtrack(0,"")
        # return comb


            

