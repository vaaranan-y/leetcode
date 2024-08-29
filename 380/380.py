import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.valPosition = dict()


    def insert(self, val: int) -> bool:
        if(val in self.vals):
            return False
        else:
            self.vals.append(val)
            self.valPosition[val] = len(self.vals) - 1
            return True


    def remove(self, val: int) -> bool:
        if(val in self.vals):
            if(len(self.vals) == 1):
                self.vals.pop(0)
                self.valPosition.pop(val)
            else:
                valIndex = self.valPosition[val]
                replacementVal = self.vals[len(self.vals) - 1]
                self.vals[valIndex] = replacementVal
                self.vals.pop()
                self.valPosition[replacementVal] = valIndex
            return True
        else:
            return False


    def getRandom(self) -> int:
        return random.choice(self.vals)