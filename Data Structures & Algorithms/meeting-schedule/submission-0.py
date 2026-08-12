"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        prevTime = 0
        for interval in intervals:
            if prevTime > interval.start:
                return False
            prevTime = interval.end

        return True