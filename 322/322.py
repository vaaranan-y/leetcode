class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = dict()
        cache[amount] = 0

        for i in range(amount - 1, -1, -1):
            currMinDist = float("inf")
            for coin in coins:
                if(i + coin in cache):
                    currMinDist = min(currMinDist, cache[i + coin] + 1)
            cache[i] = currMinDist
        
        if(cache[0] == float("inf")):
            return -1
        else:
            return cache[0]

