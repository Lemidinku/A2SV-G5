class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next, new_node.prev = new_node, self.curr
        self.curr = self.curr.next
        

    def back(self, steps: int) -> str:
        new_curr = self.curr
        curr_step = 0
        while curr_step<steps and new_curr.prev:
            new_curr = new_curr.prev
            curr_step +=1
    
        self.curr = new_curr
        return self.curr.val


    def forward(self, steps: int) -> str:
        new_curr = self.curr
        curr_step = 0
        while new_curr.next and curr_step<steps:
            new_curr = new_curr.next
            curr_step +=1

        self.curr = new_curr
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)