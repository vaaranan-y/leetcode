class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while(x or y):
            res += x % 2 != y % 2
            x = x >> 1
            y = y >> 1
        
        return res