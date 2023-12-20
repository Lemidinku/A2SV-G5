class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        # if k>len(s): return s
        word = list(s)

        def rev(arr,start,end):
            while start<end:
                arr[start],arr[end] = arr[end], arr[start]
                start+=1
                end-=1


        i =0
        while i+k-1 < n:
            rev(word,i,i+k-1)
            i += 2*k
        rev(word,i,n-1)

        return "".join(word)