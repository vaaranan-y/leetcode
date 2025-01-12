class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if(x < 0):
            isNeg = True
            x *= -1
        res = 0
        bound = (2**31)//10
        lastDigMax = (2**31 - 1) % 10
        lastDigMin = int(math.fmod(-2**31, 10)) * -1
        while(x):
            if(res > bound):
                return 0
            elif(res == bound and not isNeg and x > lastDigMax):
                return 0
            elif(res == bound and isNeg and x > lastDigMin):
                return 0
            else:
                digToAdd = x % 10
                x = x // 10
                res *= 10
                res += digToAdd

        if(isNeg):
            return res*-1
        else:
            return res
        