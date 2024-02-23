# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def validate(node):
            if not node:
                return float("inf"),float("-inf"),True,0
            
            
            min_left , max_left, valid_left,left_sum = validate(node.left)
            min_right , max_right, valid_right,right_sum= validate(node.right)

            maxx = max(max_left, max_right, node.val)
            minn = min(min_left, min_right, node.val)
            isValid = max_left<node.val<min_right and valid_left and valid_right
            summ = node.val + left_sum+right_sum
            if isValid:
                self.max = max(self.max, summ)
            
            return minn, maxx, isValid,summ

        validate(root)

        return self.max


            



