class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        resStack = []
        for digit in num:
            while(k > 0 and len(resStack) > 0 and resStack[-1] > digit):
                k -= 1
                resStack.pop()
                
            if(len(resStack) == 0 and digit == "0"):
                continue
            resStack.append(digit)
        # However many chars we need to pop still, remove them from the end
        
        resStack = resStack[:len(resStack) - k]
        

        res = "".join(resStack)
        if(res == ""):
            return "0"
        return res.lstrip("0")