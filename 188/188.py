class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        states = [0]*(2*k)

        states[0] = -prices[0]
        for i in range(1, len(states)):
            states[i] = float('-inf')
        
        for price in prices:
            prev = 0
            enteringMarket = True
            for i in range(len(states)):
                if(enteringMarket):
                    states[i] = max(states[i], prev - price)
                else:
                    states[i] = max(states[i], prev + price)
                enteringMarket = not enteringMarket
                prev = states[i]
        
        return states[len(states) - 1]
        