class FrontMiddleBackQueue:
    
    def __init__(self):
        self.queue = []
        

    def pushFront(self, val: int):
        self.queue.insert(0,val)

    def pushMiddle(self, val: int):
        self.queue.insert(len(self.queue) // 2,val)

    def pushBack(self, val: int):
        self.queue.append(val)

    def popFront(self):
        return (self.queue or [-1]).pop(0)

    def popMiddle(self):
        return (self.queue or [-1]).pop((len(self.queue)-1)//2)

    def popBack(self):
        return (self.queue or [-1]).pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()