# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.new_head = None
        def reverse(node):
            if not node:
                return None
            if not node.next:
                self.new_head = node
                return node
            curr = reverse(node.next)
            curr.next, node.next = node, None
            return node
        reverse(head)
        return self.new_head


