class Solution:
    def canJump(self, nums: List[int]) -> bool:
        toReach = nums[len(nums) - 1] # This is where we need to get to currently (starts as the last index, which is our goal)

        for i in range(len(nums) - 1, -1, -1):
            if(i + nums[i] >= toReach): # Check if we can reach our goal from current index (i.e. the furthest index we can reach is the current index plus the jump distance)
                toReach = i # Now we have a new goal, which is the current index, since the current index can reach our original goal
        
        return toReach == 0 # We have back tracked to what would be our starting position