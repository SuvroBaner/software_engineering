class LongestPeak:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(m) where m are the number of peaks
    def solution1(self):
        peak_idx = []
        for i in range(1, len(self.array) - 1):
            leftNum = self.array[i-1]
            midNum = self.array[i]
            rightNum = self.array[i+1]
            if (midNum > leftNum and midNum > rightNum):
                peak_idx.append(i)
        
        longest_peak = 0
        for idx in peak_idx:
            peak_length = 1
            midIdx = idx
            while ((midIdx - 1) >= 0 and self.array[midIdx] > self.array[midIdx - 1]):
                peak_length += 1
                midIdx -= 1 

            midIdx = idx
            while ((midIdx + 1) < len(self.array) and self.array[midIdx] > self.array[midIdx + 1]):
                peak_length += 1
                midIdx += 1

            if peak_length > longest_peak:
                longest_peak = peak_length
        
        return longest_peak

# Testing the solution -
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# array = []
# array = [1, 2, 3, 4]
# array = [1, 2, 2]
obj = LongestPeak(array)
print(obj.solution1())