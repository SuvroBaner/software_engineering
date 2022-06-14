class MergeOverlappingInterval:
    def __init__(self, intervals):
        self.intervals = intervals

    # Time : O(nlogn) | Space : O(n)
    def solution(self):
        self.intervals.sort()
        result = []
        for i in range(len(self.intervals) - 1):
            first = self.intervals[i]
            second = self.intervals[i + 1]
            if first[1] >= second[0]:
                self.intervals[i+1] = [first[0], second[1] if second[1] > first[1] else first[1]]
            else:
                result.append(first)
        return result + [self.intervals[-1]]

# Testing the solution -

intervals = [[4, 7], [1, 2], [3, 5], [6, 8], [9, 10]]
obj = MergeOverlappingInterval(intervals)
print(obj.solution())          