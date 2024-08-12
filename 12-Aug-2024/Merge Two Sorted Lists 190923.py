# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check if either of the list is empty
        if not list1 or not list2:
            return list1 or list2
     
        elif list1.val<list2.val:
            temp = list1
            temp.next = self.mergeTwoLists(list1.next,list2)
            return temp
        else:
            temp = list2
            temp.next = self.mergeTwoLists(list1,list2.next)
            return temp
