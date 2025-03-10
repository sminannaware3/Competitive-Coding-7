#Best Example: [[5,10],[3,10],[1,10],[10,15],[10,20],[12,22],[25,30],[23,27]]
# Time O(nlogn + n)
# Space O(n)
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        hq = []
        for st, end in intervals:
            if len(hq) == 0:
                heappush(hq, end)
            else:
                if hq[0] <= st: 
                    heappop(hq)
                heappush(hq, end)
        return len(hq)

# Time O(n + 2n)
# Space O(2n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = defaultdict(int)
        end = defaultdict(int)
        times = []
        for st, e in intervals:
            start[st] += 1
            end[e] += 1
            times.append(st)
            times.append(e)
        times.sort()
        prevT = -1
        count = 0
        maxCount = 0
        for t in times:
            if t == prevT: continue
            if t in start: 
                count += start[t]
            if t in end: count -= end[t]
            maxCount = max(maxCount, count)
            prevT = t
        return maxCount

# Time O(2n)
# Space O(2n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for st, e in intervals:
            start.append(st)
            end.append(e)
        start.sort()
        end.sort()
        endIndex = 0
        roomInUse = 0
        available = 0
        for st in start:
            if st < end[endIndex]: 
                if available == 0: roomInUse += 1
                else: available -= 1
            else: 
                while st >= end[endIndex]:
                    available += 1
                    endIndex += 1
                available -= 1
        return roomInUse

                