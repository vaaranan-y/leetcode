class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        count = 0
        for num in nums:
            if(k - num in seen and seen[k - num] > 0):
                seen[k - num] -= 1
                count += 1
            else:
                seen[num] += 1
        
        return count
        