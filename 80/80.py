# Problem: 80. Removed Duplicates from Sorted Array II
# Vaaranan Yogalingam
# 2024-08-17

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1 = 0 # Explorer
        p2 = 0 # Anchor
        currVal = nums[p1]
        count = 0

        while(p1 < len(nums)):
            while(p1 < len(nums) and currVal == nums[p1]):
                count += 1
                p1 += 1
            count = min(count, 2)
            for i in range(count):
                nums[p2] = currVal
                p2 += 1
            count = 0
            if(p1 < len(nums)):
                currVal = nums[p1]

        return p2

        