class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        curr = n
        while(curr % 3 == 0 and curr != 0):
            curr = curr / 3
        
        return curr == 1
        