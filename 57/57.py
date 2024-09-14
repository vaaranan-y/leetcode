class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        currInterval = newInterval
        for i in range(len(intervals)):
            interval = intervals[i]

            if(currInterval[1] < interval[0]):
                res.append(currInterval)
                currInterval = interval
                continue # No overlap
            elif(currInterval[0] > interval[1]):
                res.append(interval)
                continue # No overlap
            else:
                currInterval = [min(interval[0], currInterval[0]), max(interval[1], currInterval[1])]
        
        res.append(currInterval)
        return res
