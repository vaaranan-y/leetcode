class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        currPair = [price, 1]
        while(len(self.stack) > 0):
            topPair = self.stack[-1] 
            if(topPair[0] <= currPair[0]):
                currPair[1] += topPair[1]
                self.stack.pop(len(self.stack) - 1)
            else:
                break
        self.stack.append(currPair)
        return currPair[1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)