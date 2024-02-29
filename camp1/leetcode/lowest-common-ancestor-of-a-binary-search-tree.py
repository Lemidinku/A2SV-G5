# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minn = min(p.val,q.val)
        maxx = max(p.val,q.val)

        if minn <= root.val<= maxx:
            return root
        if minn>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return self.lowestCommonAncestor(root.left,p,q)
            
            