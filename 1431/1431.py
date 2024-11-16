class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currMax = max(candies)
        res = []

        for candyCount in candies:
            if(candyCount + extraCandies >= currMax):
                res.append(True)
            else:
                res.append(False)
        
        return res
