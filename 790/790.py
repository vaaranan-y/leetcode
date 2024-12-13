class Solution:
    def numTilings(self, n: int) -> int:
        goal = 2 * n
        cache = [0]*(max(goal + 1, 5))
        cache[0] = 0
        cache[1] = 0
        cache[2] = 1
        cache[3] = 1
        cache[4] = 2

        for i in range(5, goal + 1):
            if(i % 2 == 0):
                cache[i] = (cache[i - 2] + cache[i - 3] + cache[i - 3] +  cache[i - 4]) % (10**9 + 7)
            else:
                cache[i] = (cache[i - 2] + cache[i - 3]) % (10**9 + 7)
        
        return cache[goal] 

        