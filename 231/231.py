class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        possInv = n - 1

        return n > 0 and not(n & possInv)

         