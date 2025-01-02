class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        valSum = 0
        for i in range(n + 1):
            valSum += i
        
        for i in range(len(nums)):
            valSum -= nums[i]
        
        return valSum
        