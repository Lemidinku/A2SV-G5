# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level = defaultdict(list)

        def dfs(node,height):
            if node:
                self.level[height].append(node.val)
                dfs(node.left,height+1)
                dfs(node.right,height+1)
        dfs(root,0)


        for level_num,level in self.level.items():
            if not level_num%2: continue
            left = 0
            right = len(level)-1
            while left<right:
                level[left],level[right] = level[right], level[left]
                left+=1
                right -=1

        return [b for b in self.level.values()]