class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda interval: interval[0])
        res = []
        currInterval = intervals[0] 
        
        for i in range(1, len(intervals)):
            if(currInterval[1] >= intervals[i][0]):
                currInterval[1] = max(currInterval[1], intervals[i][1])
            else:
                res.append(currInterval)
                currInterval = intervals[i]
        res.append(currInterval)
        return res



