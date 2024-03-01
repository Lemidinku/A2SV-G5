# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = Node(float("-inf"))
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val < prev.val:
                node1, node2 = dummy, dummy.next
                while not(node1.val<=curr.val<=node2.val):
                    node1=node1.next
                    node2=node2.next
                temp = curr.next
                curr.next, node1.next= node2,curr
                prev.next = temp
                curr = temp
                
            else:
                prev  = prev.next
                curr = curr.next
        
        return dummy.next