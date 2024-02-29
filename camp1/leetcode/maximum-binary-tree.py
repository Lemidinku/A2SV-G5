# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def construct(nums,left,right):
            if left>right:
                return 
            maxx = max(nums[left:right+1])
            max_ind= nums.index(maxx)

            node = TreeNode(maxx)

            node.left = construct(nums,left, max_ind-1)
            node.right = construct(nums,max_ind+1, right)
        
            return node
        
        return construct(nums,0, len(nums)-1)

            