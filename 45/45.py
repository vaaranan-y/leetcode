class Solution:
    def jump(self, nums: List[int]) -> int:
        # Perform a BFS where each index is a node, and the way to get to those nodes (branches) is by a certain number of jumps from 1 to nums[i]
        count = 0
        leftBound = 0
        rightBound = 0

        while(rightBound < len(nums) - 1):
            furthestPoint = 0
            for i in range(leftBound, rightBound + 1):
                furthestPoint = max(i + nums[i], furthestPoint)
            leftBound = rightBound + 1
            rightBound = furthestPoint
            count += 1
        
        return count


