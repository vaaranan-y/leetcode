class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProfit = 0
        profit = 0
        for i in range(1, len(prices)):
            if(prices[i] > prices[i - 1]):
                currProfit += prices[i] - prices[i - 1]
            else:
                profit += currProfit
                currProfit = 0

        profit += currProfit
        return profit

