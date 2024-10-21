class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        while(l <= r):
            m = (l + r)//2
            if(nums[m] == target):
                return m
            
            if(nums[l] <= nums[m]): # We are in the second portion of nums on the left
                if(target < nums[l] or target > nums[m]):
                    l = m + 1
                else:
                    r = m - 1
            else:  # We are in the second portion of nums on the right
                if(target > nums[r] or target < nums[m]):
                    r = m - 1
                else:
                    l = m + 1
        
        return -1