class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])

        p1 = 0
        p2 = 1
        count = 0
        while(p2 < len(intervals)):
            if(intervals[p1][1] > intervals[p2][0]):
                if(intervals[p2][1] < intervals[p1][1]):
                    p1 = p2
                p2 += 1
                count += 1
            else:
                p1 = p2
                p2 += 1
        
        return count

        