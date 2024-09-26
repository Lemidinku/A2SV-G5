# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.lis = []
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.lis)<self.size:
            self.lis.insert(0,value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.lis)<self.size:
            self.lis.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        if len(self.lis):
            self.lis.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if len(self.lis):
            self.lis.pop()
            return True
        return False
        

    def getFront(self) -> int:
        if self.lis: return self.lis[0]
        return -1      

    def getRear(self) -> int:
        if self.lis: return self.lis[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.lis)==0
        

    def isFull(self) -> bool:
        return len(self.lis)==self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()