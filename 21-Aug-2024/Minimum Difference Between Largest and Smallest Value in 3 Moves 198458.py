# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        new_curr = dummy
        curr= head
        
        while curr.next:
            if curr.val ==0:
                new_curr.next = ListNode(0)
                new_curr = new_curr.next
            else:
                new_curr.val += curr.val
            curr = curr.next
        return dummy.next


        