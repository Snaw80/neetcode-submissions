"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        i = 1
        while i < len(intervals) and intervals[i-1].end <= intervals[i].start:
            i += 1
        return not intervals or i == len(intervals)