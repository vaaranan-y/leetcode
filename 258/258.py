class Solution:
    def addDigits(self, num: int) -> int:
        while(num // 10 != 0):
            temp = 0
            while(num):
                temp += num % 10
                num = num // 10
            num = temp
        
        return num

        