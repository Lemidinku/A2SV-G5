# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []

        def traverse(root):
            if not root:
                return 
            if len(self.heap) < k:
                heapq.heappush(self.heap, -root.val)

            elif self.heap[0] < -root.val:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, -root.val)


            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return -self.heap[0]