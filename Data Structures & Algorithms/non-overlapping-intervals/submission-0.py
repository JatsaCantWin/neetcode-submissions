class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        result = 0

        intervals.sort()
        rightmostPoint = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= rightmostPoint:
                rightmostPoint = end
            else:
                result += 1
                rightmostPoint = min(end, rightmostPoint)
                
        return result