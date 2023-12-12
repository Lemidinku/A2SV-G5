class OrderedStream:

    def __init__(self, n: int):
        self.stream = {}
        self.curr_key = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []
        while self.curr_key in self.stream:
            result.append(self.stream[self.curr_key])
            self.curr_key+=1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)