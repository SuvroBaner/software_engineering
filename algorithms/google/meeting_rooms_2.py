from typing import List

class Solution:
    # Time : O(nlogn) | Space : O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        s, e = 0, 0
        count, result = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)
        
        return result

sol = Solution()
intervals = [[7, 10], [2, 4]]
intervals = [[0, 30], [5, 10], [15, 20]]
intervals = [[0, 30], [5, 10], [15, 20], [21, 25]]
intervals = [[9,10],[4,9],[4,17]]
intervals = [[0, 30], [5, 10], [15, 20], [21, 32], [31, 50]]
print(sol.minMeetingRooms(intervals))