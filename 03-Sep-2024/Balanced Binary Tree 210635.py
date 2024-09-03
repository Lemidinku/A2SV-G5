# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: return True, 0

            left_balanced, left_depth = dfs(node.left)
            right_balanced, right_depth = dfs(node.right)

            balanced = abs(left_depth-right_depth)<=1 and left_balanced and right_balanced

            return balanced, 1 + max(left_depth, right_depth)

        
        return dfs(root)[0]

