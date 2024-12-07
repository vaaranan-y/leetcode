class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0,1,1]

        for i in range(3, n + 1):
            print(cache)
            cache[i % 3] = sum(cache)
        
        return cache[n % 3]