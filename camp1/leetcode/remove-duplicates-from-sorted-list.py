# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next): return head
        left = head
        right = head.next

        while right:
            if left.val == right.val:
                left.next = right.next
                right = right.next
            else:
                left = left.next
                right = right.next
        return head





