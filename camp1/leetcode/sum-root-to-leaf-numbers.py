# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0
    def sumNumbers(self, root: Optional[TreeNode],val = 0) -> int:
        if not (root.left or root.right):
            self.answer += (10 *val)+root.val
            return self.answer
        
        if root.left:self.sumNumbers(root.left,(10 *val)+root.val)
        if root.right:self.sumNumbers(root.right,(10 *val)+root.val)

        return self.answer


        
        