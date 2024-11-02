class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = [0]*(len(triangle) + 1)

        for row in range(len(triangle) - 1, -1, -1):
            for i in range(row + 1):
                cache[i] = triangle[row][i] + min(cache[i], cache[i + 1])

        return cache[0]
        