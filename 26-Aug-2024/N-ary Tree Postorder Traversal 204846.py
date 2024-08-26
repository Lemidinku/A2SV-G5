# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if not root: return []
        traversal = []
        stack = [root]
        while stack:
            curr = stack.pop()
            
            for child in curr.children:
                stack.append(child)
            traversal.insert(0,curr.val)
        
        return traversal


        