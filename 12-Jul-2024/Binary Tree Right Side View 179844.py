# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.level = defaultdict(int)

        def dfs(node,height=0):
            if node:
                if height not in self.level:
                    self.level[height] = node.val
                dfs(node.right,height+1)
                dfs(node.left,height+1)
        dfs(root)

        sideView = [level for level in self.level.values()]
           
        return sideView