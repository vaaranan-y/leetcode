class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        actualK = k % len(nums)

        # Reverse whole list
        l = 0
        r = len(nums) - 1

        while(l <= r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
        
        # Reverse again 0 to k - 1, and then k to n - 1
        l1 = 0
        r1 = actualK - 1

        while(l1 <= r1):
            temp = nums[l1]
            nums[l1] = nums[r1]
            nums[r1] = temp
            l1 += 1
            r1 -= 1
        
        l2 = actualK
        r2 = len(nums) - 1

        while(l2 <= r2):
            temp = nums[l2]
            nums[l2] = nums[r2]
            nums[r2] = temp
            l2 += 1
            r2 -= 1
        
