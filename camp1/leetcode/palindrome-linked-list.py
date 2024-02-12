# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        mid = slow

        self.head2 = None
        def reverse(node):
            if not node:
                return None
            if not node.next:
                self.head2 = node
                return node
            curr = reverse(node.next)
            curr.next, node.next = node, None
            return node
        

        reverse(mid)
        node1,node2 = head,self.head2

        while node2:
            if node1.val != node2.val:
                return False
            node1=node1.next
            node2 = node2.next
        return True
            

        