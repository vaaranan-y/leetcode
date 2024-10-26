class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        larger = nums1 if (len(nums1) > len(nums2)) else nums2
        smaller = nums2 if (len(nums1) > len(nums2)) else nums1

        l = 0
        r = len(smaller) - 1
        leftPartLen = (len(larger) + len(smaller)) // 2

        while True:
            m = (l + r)//2
            x = m
            y = leftPartLen - x - 2

            smallerEdge = float("-infinity") if x < 0 else smaller[x]
            smallerAdj = float("infinity") if x + 1 >= len(smaller) else smaller[x + 1]
            largerEdge = float("-infinity") if y < 0 else larger[y]
            largerAdj = float("infinity") if y + 1 >= len(larger) else larger[y + 1]

            if(largerEdge > smallerAdj):
                l = m + 1
            elif(largerAdj < smallerEdge):
                r = m - 1
            else:
                if((len(nums1) + len(nums2)) % 2 == 0):
                    return (max(smallerEdge, largerEdge) + min(smallerAdj, largerAdj)) / 2
                else:
                    return min(smallerAdj, largerAdj)

        