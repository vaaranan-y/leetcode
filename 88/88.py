class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:

        # Old Solution
        # if(nums2 == []):
        #     return nums1

        # for i in range(len(nums1) - len(nums2)):
        #     if(nums1[i] > nums2[0]):
        #         temp1 = nums1[i]
        #         nums1[i] = nums2[0]
        #         nums2[0] = temp1

        #         # insert nums1 value into nums2
        #         for j in range(1, len(nums2)):
        #             if(nums2[j] < nums2[j - 1]):
        #                 temp2 = nums2[j]
        #                 nums2[j] = nums2[j - 1]
        #                 nums2[j - 1] = temp2

        

        # for i in range(len(nums1) - len(nums2), len(nums1)):
        #     nums1[i] = nums2[i - len(nums1) + len(nums2)]


        # Better Solution
        p1 = len(nums1) - len(nums2) - 1
        p2 = len(nums2) - 1

        for i in reversed(range(len(nums1))):
            if(p1 == -1):
                nums1[i] = nums2[p2]
                p2 -= 1
            elif(p2 == -1):
                nums1[i] = nums1[p1]
                p1 -= 1
            elif(nums1[p1] >= nums2[p2]):
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1