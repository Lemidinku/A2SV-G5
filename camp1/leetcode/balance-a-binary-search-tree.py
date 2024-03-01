# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        traversal= []
        def intrav(node):
            if node:
                intrav(node.left)
                traversal.append(node.val)
                intrav(node.right)
        intrav(root)
        def createHeightBalanced(arr,left,right):
            if left>right:
                return 
            
            mid = (right+left)//2
            node = TreeNode(arr[mid])
            node.left =  createHeightBalanced(arr,left,mid-1)
            node.right =  createHeightBalanced(arr,mid+1,right)
            return node
        return createHeightBalanced(traversal, 0, len(traversal)-1)
        