class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if(x == 0):
                return 0
            elif(n == 0):
                return 1
            else:
                newExp = n // 2
                partPow = helper(x, newExp)
                refactor = n - 2*newExp
                return  partPow * partPow * (x**refactor)
        
        if(n < 0):
            return 1/helper(x, abs(n))
        else:
            return helper(x, abs(n))
        

        