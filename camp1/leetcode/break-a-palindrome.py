class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n  = len(palindrome)
        if n<2: return ""
        arr = list(palindrome)

        changed = -1
        for i in range(n//2):
            
            if arr[i]!="a":
                changed = i
                break

        if changed!=-1:
            arr[changed]= "a"
        else:
            arr[-1] = "b"

        return "".join(arr)
        

        