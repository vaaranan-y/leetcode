class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 0
        while(r < len(nums)):
            if(nums[l] == val):
                # send the right pointer out to find a replacement
                while(r < len(nums) and nums[r] == val):
                    r += 1
                if(r == len(nums)):
                    return l
                else:
                    nums[l] = nums[r]
                    nums[r] = val
                    l += 1
                    r += 1
            else:
                l += 1
                r += 1
        return l