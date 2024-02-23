# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validate(node):
            if not node:
                return float("inf"),float("-inf"),True
            
            
            min_left , max_left, valid_left = validate(node.left)
            min_right , max_right, valid_right= validate(node.right)

            maxx = max(max_left, max_right, node.val)
            minn = min(min_left, min_right, node.val)
            isValid = max_left<node.val<min_right and valid_left and valid_right
            
            return minn, maxx, isValid

        return validate(root)[2]


