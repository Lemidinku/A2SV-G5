# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversal = defaultdict(list)
        def traverse(node, col=0, row=0):

            if not node:
                return
            
            self.traversal[(col,row)].append(node.val)
            traverse(node.left, col-1, row+1)
            traverse(node.right, col+1, row+1)
            
        
        traverse(root)
        result = [(a,b) for a,b in self.traversal.items()]
        result.sort()
        ans = defaultdict(list)
        for pos, nums in result:
            nums.sort()
            ans[pos[0]].extend(nums)
        return [b for _,b in ans.items()]


        