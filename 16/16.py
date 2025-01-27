class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closestSum = float("inf")
        closestSumDist = float("inf")
        nums = sorted(nums)
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1

            while(lo < hi):
                currSum = nums[i] + nums[lo] + nums[hi]
                
                # Compare to closest sum
                if(abs(currSum - target) < closestSumDist):
                    closestSum = currSum
                    closestSumDist = abs(currSum - target)
                
                # Update pointers
                if(currSum > target):
                    hi -= 1
                elif(currSum < target):
                    lo += 1
                else: # If they are equal, this is the best case scenario, 0 off
                    return currSum
        
        return closestSum