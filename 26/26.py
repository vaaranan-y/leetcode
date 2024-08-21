class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        while(p1 < len(nums)):
            currVal = nums[p2]
            while(p1 < len(nums) and nums[p1] == currVal):
                p1 += 1
            if(p1 < len(nums)):
                p2 += 1
                nums[p2] = nums[p1]
        
        return p2 + 1 # Add the 1 because p2 ends at the correct spot (so actual zero-indexed value is not correct length)