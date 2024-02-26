# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.count = defaultdict(int)

        def find_modes(node):
            if node:
                self.count[node.val] +=1
                find_modes(node.left)
                find_modes(node.right)

        find_modes(root)

        modes = []
        max_count = 0
        for num,count in self.count.items():
            if count > max_count:
                modes=[num]
                max_count = count
            elif count==max_count:
                modes.append(num)

        return modes


        



