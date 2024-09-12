class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while(True):
            if(n in seen):
                return False
            else:
                seen.add(n)
                strn = str(n)
                squaredSum = 0
                for digit in strn:
                    squaredSum += int(digit)**2
                
                if(squaredSum == 1):
                    return True
                n = squaredSum
                

