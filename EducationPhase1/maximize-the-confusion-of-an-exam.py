class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true = 0
        max_len =0
        left = 0
        for right in range(len(answerKey)):
            if answerKey[right]=="T": true+=1
        
            while min(true, right-left+1-true) > k :
                if answerKey[left]=="T": true-=1
                left+=1
            
            max_len = max(max_len, right-left+1)
        return max_len