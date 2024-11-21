class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countMap = defaultdict(int)

        for num in arr:
            countMap[num] += 1
        
        countSet = set()
        for key in countMap:
            if(countMap[key] in countSet):
                return False
            countSet.add(countMap[key])

        return True
        