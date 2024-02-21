class Solution:
    def decodeString(self, s: str) -> str:
        
        def decode(st,n):
            if st.isalpha():
                return st*n
            res = ""
            opened = 0
            num = 0
            curr_st = ""
            for i in range(len(st)):
                if st[i].isdigit():
                    if num==0: 
                        num = int(st[i])
                    elif st[i-1].isdigit() and opened==0: 
                        num = int(str(num)+str(st[i]))
                    else: curr_st+=st[i]
                elif st[i] == "[":
                    if opened>0: curr_st+=st[i]
                    opened +=1
                elif st[i] == "]" :
                    opened -=1
                    if opened>0: curr_st+=st[i]
                    if opened==0:
                        res += decode(curr_st,num)
                        curr_st = ""
                        num=0
                    
                else:
                    if num==0: res+=st[i]
                    else: curr_st+=st[i]
            return res*n
        return decode(s,1)