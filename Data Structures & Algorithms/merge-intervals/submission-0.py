class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()

        newInterval = None

        for interval in intervals:
            if not newInterval:
                newInterval = interval
                continue

            if newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
                continue

            newInterval[1] = max(newInterval[1], interval[1])

        if newInterval:
            result.append(newInterval)

        return result