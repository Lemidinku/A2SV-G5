# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.maxDiff = 0

        def min_max(root):
            if not (root.left or root.right):
                return root.val, root.val

            

            if root.left and not root.right:
                left_min, left_max = min_max(root.left)
                left_diff = max(abs(root.val-left_min), abs(root.val-left_max))
                self.maxDiff = max(self.maxDiff, left_diff)
                return min(root.val, left_min), max(root.val, left_max)

            if root.right and not root.left:
                right_min, right_max = min_max(root.right)
                right_diff = max(abs(root.val-right_min), abs(root.val-right_max))
                self.maxDiff = max(self.maxDiff,right_diff)
                return min(root.val, right_min), max(root.val, right_max)


            left_min, left_max = min_max(root.left)
            right_min, right_max = min_max(root.right)
            left_diff = max(abs(root.val-left_min), abs(root.val-left_max))
            right_diff = max(abs(root.val-right_min), abs(root.val-right_max))

            self.maxDiff = max(self.maxDiff, left_diff, right_diff)

            return min(root.val, left_min, right_min), max(root.val, left_max, right_max)

        min_max(root)
        return self.maxDiff
