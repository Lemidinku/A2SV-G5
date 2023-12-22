class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.next_dir = {(1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0)}
        self.dir_name = {(1,0):"East", (-1,0):"West", (0,1):"North", (0,-1):"South"}
        self.pos = (0,0)
        self.dir = (1,0)
    
    def inbound(self, x,y):
        return 0<=x<self.width and 0<=y<self.height

    def step(self, num: int) -> None:
        num %= (2*self.width + 2*(self.height-2))
        if num==0 and self.pos == (0,0):
            self.dir = (0,-1)

        for _ in range(num):
            x,y = self.pos[0]+self.dir[0] ,self.pos[1]+self.dir[1]

            if self.inbound(x,y):
                self.pos = (x,y)
            else:
                dir = self.next_dir[self.dir]
                self.pos = (self.pos[0]+dir[0], self.pos[1]+dir[1])
                self.dir = dir
        

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir_name[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()