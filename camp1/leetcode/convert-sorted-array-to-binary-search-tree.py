# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createHeightBalanced(arr,left,right):
            if left>right:
                return 
            
            mid = (right+left)//2
            node = TreeNode(arr[mid])
            node.left =  createHeightBalanced(arr,left,mid-1)
            node.right =  createHeightBalanced(arr,mid+1,right)
            return node
        
        return createHeightBalanced(nums,0,len(nums)-1)
