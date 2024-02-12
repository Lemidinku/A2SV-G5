class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self, head=None):
        self.head = head
        

    def get(self, index: int) -> int:

        i = 0
        curr = self.head
        while curr:
            if index==i:
                return curr.val
            curr = curr.next
            i+=1
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        self.head, new_head.next = new_head, self.head

        

    def addAtTail(self, val: int) -> None:
    
        new_node = Node(val)
        curr = self.head
        if not curr: 
            self.head = new_node
            return
        while curr.next:
            curr = curr.next

        curr.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node("*")
        dummy.next = self.head
        new_node = Node(val)
        curr = dummy
        if index==0:
            self.head, new_node.next = new_node, self.head
            return
        i = 0
        while curr.next:
            if i==index: 
                break
            curr = curr.next
            i+=1
        if i==index: 
            curr.next, new_node.next = new_node, curr.next
        



    def deleteAtIndex(self, index: int) -> None:
        if not self.head: return
        if index == 0 and self.head:
            self.head = self.head.next
            return

        prev = None
        curr = self.head
        i = 1
        while curr.next:
            prev,curr = curr, curr.next
            if i==index:
                prev.next = curr.next
                return
            i+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)