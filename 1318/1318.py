class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while(c or a or b):
            if(a % 2 | b % 2 == 0 and c % 2 == 1):
                count += 1
            elif(a % 2 | b % 2 == 1 and c % 2 == 0):
                if(a % 2 & b % 2 == 1):
                    count += 2
                else:
                    count += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return count
        