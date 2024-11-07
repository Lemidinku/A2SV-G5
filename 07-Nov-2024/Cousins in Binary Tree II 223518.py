# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        queue = deque()
        queue.append((root,0))

        while queue:
            summ = 0
            for i in range(len(queue)):
                summ += queue[i][0].val

            for _ in range(len(queue)):
                node, sibling = queue.popleft()
                node.val = summ-sibling-node.val
                if node.left and node.right:
                    queue.append((node.left, node.right.val))
                    queue.append((node.right, node.left.val))
                elif node.left: 
                    queue.append((node.left, 0))
                elif node.right:
                    queue.append((node.right,0))
        return root