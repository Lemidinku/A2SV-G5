class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        ind_table = {val:i for i,val in enumerate(nums)}
        for old,new in operations:
            ind_table[new] = ind_table.pop(old)

        result = [0]*len(nums)
        for num,ind in ind_table.items():
            result[ind] = num
        return result











        # replace_with = {x:x for x in nums}
        # for old,new in operations:
        #     replace_with[old] = new
        #     print(replace_with)
        # return [replace_with[a] for a in nums]
