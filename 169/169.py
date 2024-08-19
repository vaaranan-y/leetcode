# Problem: 169. Majority Element
# Vaaranan Yogalingam
# 2024-08-18

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # threshold = math.floor(len(nums)/2)

        # numsFound = dict()

        # for num in nums:
        #     if(num in numsFound):
        #         numsFound[num] += 1
        #     else:
        #         numsFound[num] = 1

        # for num in numsFound:
        #     if(numsFound[num] > threshold):
        #         return num

        # Second attempt (O(1) space)
        result = nums[0]
        count = 1

        for i in range(1, len(nums)):
            num = nums[i]

            if(num == result):
                count += 1
            else:
                if(count != 0):
                    count -= 1
                else:
                    result = num
                    count = 1
        
        return result