# Time O(nxn log k) k could be n^2
# Space O(k)
from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq = []
        for i in matrix:
            for j in i:
                if len(hq) == k and j > -hq[0] : break
                heappush(hq, -j)
                if len(hq) > k: heappop(hq)
        return -heappop(hq)

# Binary search
# Time O(log(max-min) * n log n)
# Space O(1)
# Question: How does low and high is always present in matrix but mid may or may not? for initial range binary search
from typing import List
from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        high = matrix[-1][-1]
        low = matrix[0][0]
        while low <= high:
            mid = low + (high - low) // 2
            c = self.getCount(matrix, mid) # n log n
            #if c == k: return mid -- we cannot return mid as mid might not exist in matrix
            if c >= k:
                high = mid - 1
            else: low = mid + 1 
        return low
    
    def getCount(self, matrix: List[List[int]], n: int) -> int:
        count = 0
        for i in matrix: #for each row  O(n) *
            count += self.findLastOccurance(i, n) # log n
        return count


    # find index of last element which is less than or equal to target in a sorted array
    def findLastOccurance(self, num: List[int], target: int) -> int:
        low = 0
        high = len(num) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if num[mid] <= target and (mid+1 >= len(num) or num[mid+1] > target): return mid + 1
            elif num[mid] <= target: low = mid + 1
            else: high = mid - 1
        return low