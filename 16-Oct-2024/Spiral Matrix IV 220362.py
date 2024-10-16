# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1]*n for _ in range(m)]
        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        boundaries = [-1, n,m,-1]
        curr_node = head
        pos = (0,0)
        curr_dir = 0
        while curr_node:
            matrix[pos[0]][pos[1]] = curr_node.val
            curr_node= curr_node.next

            ind = (curr_dir + 1) % 2
            amount = -1 if curr_dir > 1 else 1
            bound_update = -1 if curr_dir in [1,2] else 1


            if pos[ind]+amount==boundaries[(curr_dir + 1) % 4]:
                curr_dir =(curr_dir + 1) % 4
                pos = (pos[0]+dir[curr_dir][0], pos[1]+dir[curr_dir][1])
                boundaries[(curr_dir -1) % 4] += bound_update
            else:
                pos = (pos[0]+dir[curr_dir][0], pos[1]+dir[curr_dir][1])
            

        return matrix
                



