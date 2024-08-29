class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]*len(nums)
        suffixes = [1]*len(nums)
        prods = [1]*len(nums)

        prefixProd = 1
        for i in range(1, len(prefixes)):
            prefixProd *= nums[i - 1]
            prefixes[i] = prefixProd

        suffixProd = 1
        for i in range(len(suffixes) - 2, -1, -1):
            suffixProd *= nums[i + 1]
            suffixes[i] = suffixProd
        
        for i in range(len(prods)):
            prods[i] = prefixes[i] * suffixes[i]
        
        return prods



