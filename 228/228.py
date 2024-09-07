class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if(len(nums) == 0):
            return []

        ranges = []
        currRange = [nums[0]]

        for i in range(1, len(nums)):
            if(nums[i] - nums[i-1] == 1):
                currRange.append(nums[i])
            else:
                if(len(currRange) == 1):
                    ranges.append(str(currRange[0]))
                else:
                    ranges.append(str(currRange[0]) + "->" + str(currRange[len(currRange) - 1]))
                currRange = [nums[i]]
        

        if(len(currRange) == 1):
            ranges.append(str(currRange[0]))
        else:
            ranges.append(str(currRange[0]) + "->" + str(currRange[len(currRange) - 1]))

        return ranges
        