# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not (head or head.next): return head
        dummy = Node("*")
        dummy.next = head
        i = 1
        curr = dummy
        while i<left:
            curr = curr.next
            i+=1
        
        
        start = curr.next
        curr.next = None
        
        self.rev_left = None
        self.right = None

        def reverse(node,i):
            if not i:
                self.rev_left = node
                self.right =  node.next
                return node
            curr = reverse(node.next, i-1)
            curr.next, node.next = node, None
            return node

        rev_end = reverse(start, right-left)
        rev_end.next = self.right

        curr.next = self.rev_left

        return dummy.next