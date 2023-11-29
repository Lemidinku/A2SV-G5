class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        min_len = len(strs[0])
        for a in strs:
            if len(a) < min_len:
                min_len = len(a)
        common = ""
        
        for i in range(min_len):
            iscommon = True
            for word in strs[1:]:
                if word[i]!= strs[0][i]:
                    iscommon = False
                    break
            if iscommon: 
                common+= strs[0][i]
            else: break
            j = 1
            
        return common

