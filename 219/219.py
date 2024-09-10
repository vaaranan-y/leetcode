class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()

        for i in range(len(nums)):
            num = nums[i]
            if(num in seen and abs(i - seen[num]) <= k):
                return True
            else:
                seen[num] = i
                
        return False
