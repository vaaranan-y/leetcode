class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        n = len(potions)
        potions = sorted(potions)
        for spell in spells:
            l = 0
            r = n - 1
            count = 0
            while(l <= r):
                mid = (l + r)//2 
                prod = spell * potions[mid]
                if(prod >= success):
                    count = max(n - mid, count)
                    r = mid - 1
                else:
                    l = mid + 1
            res.append(count)
        
        return res