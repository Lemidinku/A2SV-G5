# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def split(node,k):
            if not node.next:
                head1,head2 = None,None
                if node.val<k:
                    head1 = node
                else: head2 = node
                return head1,head2

            head1,head2 = split(node.next,k)
            if node.val<k:
                node.next = head1
                return node,head2
            else: 
                node.next = head2
                return head1,node
        if not head: return
        head1,head2 = split(head,x)

        if not head1 or not head2: return head1 or head2
        
        curr = head1
        while curr.next:
            curr = curr.next
        curr.next = head2
        return head1