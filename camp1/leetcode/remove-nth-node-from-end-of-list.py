# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not (head or head.next): return head
        
        dummy = Node("*")
        dummy.next = head
        left = dummy
        right = head

        i = 1
        while i<n:
            right = right.next
            i+=1
        while right.next:
            left = left.next
            right = right.next

        
        left.next = left.next.next
        return dummy.next


        
        
        return head