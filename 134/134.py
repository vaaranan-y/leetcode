class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netGas = [0]*len(gas)

        for i in range(len(netGas)):
            netGas[i] = gas[i] - cost[i]
        
        if(sum(netGas) < 0):
            return -1

        index = 0
        currSum = 0
        currStart = 0

        while(index < len(netGas)):
            currSum += netGas[index]
            index += 1
            if(currSum < 0):
                currSum = 0
                currStart = index

        
        return currStart

