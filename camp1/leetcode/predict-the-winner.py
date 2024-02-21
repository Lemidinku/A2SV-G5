class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        #score = score of player A - score of player B
        def recur(left,right,score,turn):

            if left>right:
                return score >=0
            
            if not turn:
                takeLeft = recur(left+1,right, score+nums[left], (turn+1)%2)
                takeRight = recur(left,right-1, score+nums[right],(turn+1)%2)
                return takeLeft or takeRight
            else:
                takeLeft = recur(left+1,right, score-nums[left],(turn+1)%2)
                takeRight = recur(left,right-1, score -nums[right],(turn+1)%2)
                return takeLeft and takeRight

        
        return recur(0,len(nums)-1,0,0)

            