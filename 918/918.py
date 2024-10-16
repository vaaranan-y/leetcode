class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globalMax = nums[0]
        currSumMax = nums[0]

        globalMin = nums[0]
        currSumMin = nums[0]

        total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]

            currSumMax = max(nums[i], nums[i] + currSumMax)
            currSumMin = min(nums[i], nums[i] + currSumMin)

            globalMax = max(globalMax, currSumMax)
            globalMin = min(globalMin, currSumMin)
        
        if(globalMax < 0):
            return globalMax
        
        return max(total - globalMin, globalMax)
        