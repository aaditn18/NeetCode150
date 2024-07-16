
'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104'''



# Sorting before doing main functionality is often v helpful
# Beats 98.2% in runtime, 43.1% in memory

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        final = []
        curr = intervals[0]
        for interval in intervals[1:]:
            if curr[1] >= interval[0] and curr[1] <= interval[1]:
                curr[1] = interval[1]
            elif curr[1] >= interval[0]:
                continue
            else:
                final.append(curr)
                curr = interval
        final.append(curr)
        return final