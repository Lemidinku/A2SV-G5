# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        stack =[root]
        parent = dict()
        leaves = []
        while stack:
            curr = stack.pop()
            if curr.left: 
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right: 
                parent[curr.right] = curr
                stack.append(curr.right)
            if not (curr.right or curr.left): leaves.append(curr)
        self.good_pairs  =0 
        def dfs(node, dis, visited):
            if not node: return 
            visited.add(node)
            if dis:
                if node.left and node.left not in visited : 
                    dfs(node.left, dis-1, visited)
                if node.right and node.right not in visited: 
                    dfs(node.right, dis-1, visited)
                if node in parent and parent[node] not in visited:
                    dfs(parent[node], dis-1, visited)
            if not (node.left or node.right): 
                self.good_pairs+=1
                return 

        for leaf in leaves:
            dfs(leaf, distance, set())
            self.good_pairs -=1
        return self.good_pairs//2
        

            




            
            