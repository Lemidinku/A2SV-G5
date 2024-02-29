# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        minn = defaultdict(lambda : float("inf"))    
        maxx = defaultdict(lambda : float('-inf'))         
        def dfs(node,height, ind):
            if node:
                minn[height] = min(minn[height], ind)
                maxx[height] = max(maxx[height], ind)

                dfs(node.right, height+1, (2*ind)+1)
                dfs(node.left, height+1, 2*ind)


        dfs(root, 0, 0)
        maxx_width = 0
        for level in minn:
            width = maxx[level]-minn[level]+1
            maxx_width = max(maxx_width, width)

        return maxx_width
            











