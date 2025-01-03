class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""

        def compare(a, b):
            return 1 if int(str(a) + str(b)) < int(str(b) + str(a)) else -1
        
        nums = sorted(nums, key=cmp_to_key(compare))
        for num in nums:
            res += str(num)
        return str(int(res))