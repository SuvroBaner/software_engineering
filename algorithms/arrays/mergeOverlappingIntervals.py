# Time : O(nlog(n))
# Space : O(n)

def mergeOverlappingIntervals(intervals):
    intervals.sort()
    result = []
    for i in range(len(intervals)-1):
        if intervals[i][1] < intervals[i+1][0]:
            result.append(intervals[i])
        else:
            intervals[i+1][0] = intervals[i][0]
            intervals[i+1][1] = max(intervals[i+1][1], intervals[i][1])
    return result + [intervals[i+1]]
    

intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 2], [3, 5], [4, 7], [6, 8]]
print(mergeOverlappingIntervals(intervals))

intervals = [[1, 22], [-20, 30]]
print(mergeOverlappingIntervals(intervals))