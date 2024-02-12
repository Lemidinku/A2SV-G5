# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next and head.next.next): return head
        dummy = Node("*")
        dummy.next = head
        dummy_odd  = Node("*")
        dummy_even = Node("*")

        
        curr = dummy
        curr_odd = dummy_odd
        curr_even = dummy_even
        i = 0
        while curr:
            if not i:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            else:
                curr_even.next = curr
                curr_even= curr_even.next
            curr = curr.next
            i = (i+1)%2

        curr_odd.next = None
        curr_even.next = dummy_odd.next.next


        return dummy_even.next

            






        return dummy.next
            








        
