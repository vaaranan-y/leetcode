class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        
        s = s.lstrip()
        if(len(s) == 0):
            return 0
        isNeg = False
        boundVal = 2**31 - 1
        startIndex = 0
        if(s[0] == "-"):
            isNeg = True
            boundVal = -2**31
            startIndex = 1
        elif(s[0] == "+"):
            startIndex = 1
        
        for i in range(startIndex, len(s)):
            char = s[i]
            if(not char.isdigit()):
                break
            else:
                res = res*10 + int(char)
        
        return min(res, boundVal) if not isNeg else max(-1*res, boundVal)