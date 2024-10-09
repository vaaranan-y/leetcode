class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        while(l <= r):
            mid = l + (r - l)//2
            if(mid*mid == x):
                return mid
            elif(mid*mid < x):
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        return res
        