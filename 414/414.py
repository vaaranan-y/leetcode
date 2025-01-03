class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums *= -1
        for i in range(len(nums)):
            nums[i] *= -1
        print(nums)
        heapq.heapify(nums)

        count = 3
        num = 0
        maxVal = 0
        while(count and nums):
            prev = num
            num = heapq.heappop(nums)
            if(count == 3):
                maxVal = num
                count -= 1
            elif(num != prev):
                count -= 1
            

        return maxVal*-1 if count else num*-1
        