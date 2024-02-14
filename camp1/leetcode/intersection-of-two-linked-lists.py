# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        

        curr1 = headA
        size1 = 0
        while curr1:
            size1 +=1
            curr1 = curr1.next


        curr2 = headB
        size2= 0
        while curr2:
            size2 +=1
            curr2 = curr2.next

        diff = abs(size2-size1)
       

        if size2 > size1:
            longer = headB
            shorter = headA
        else:
            longer = headA
            shorter = headB


        
        while diff:
            longer =  longer.next
            diff -=1

        
        while longer:
            if longer==shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        
        return None

        


