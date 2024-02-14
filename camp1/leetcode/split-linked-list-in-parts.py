# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        size = 0
        curr = head
        while curr: 
            curr= curr.next
            size+=1

        size_part = size//k
        rem = size%k
        print("size",size_part, rem)



        result = []
        curr_head = head
        while k:
            if not curr_head:
                result.append(None)
                k-=1
                continue
            
            leng = size_part

            if rem: 
                leng+=1
                rem -=1

            curr = curr_head
            while leng-1:
                curr = curr.next
                leng -=1
            
            #update curr_head
            result.append(curr_head)

                
            curr_head = curr.next
            curr.next = None
            k-=1

        return result
        
        

        


        