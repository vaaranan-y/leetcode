class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        r = max(piles)
        l = 1

        while(l <= r):
            candidateRate = (l + r)//2
            hoursNeeded = 0
            for pile in piles:
                hoursNeeded += math.ceil(pile/candidateRate)
            if(hoursNeeded <= h):
                res = min(res, candidateRate)
                r = candidateRate - 1
            else:
                l = candidateRate + 1
        
        return res

        