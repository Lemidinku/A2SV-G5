class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = Node("s")
        self.tail = Node("e")
        self.head.next, self.tail.prev = self.tail , self.head
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        added = Node(value)
        temp = self.head.next 
        self.head.next, added.prev = added, self.head
        temp.prev, added.next = added, temp
        self.size +=1
        self.printLL()
        return True
    def deQueue(self) -> bool:
        if not self.size: return False
        removed = self.tail.prev
        self.tail.prev, removed.prev.next = removed.prev, self.tail
        self.size -=1
        return True

    def Front(self) -> int:
        if not self.size: return -1
        return self.tail.prev.val
        

    def Rear(self) -> int:
        if not self.size: return -1
        return self.head.next.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.val, end="-->")
            curr = curr.next
        print()
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()