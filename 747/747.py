class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        possibleRes = max(nums)
        res = -1
        for i in range(len(nums)):
            if(nums[i] == possibleRes):
                res = i
            elif(possibleRes < 2*nums[i]):
                return -1
        
        return res
        