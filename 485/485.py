class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsec = 0
        currConsec = 0
        for num in nums:
            if(num):
                currConsec += 1
            else:
                maxConsec = max(maxConsec, currConsec)
                currConsec = 0
        
        return max(maxConsec, currConsec)

        