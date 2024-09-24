class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        l += 1
        totalWater = 0
        while(l <= r):
            if(maxLeft < maxRight):
                totalWater += max(0, maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                totalWater += max(0, maxRight - height[r])
                maxRight = max(maxRight, height[r])
                r -= 1
        
        return totalWater
