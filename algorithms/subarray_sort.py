class SubarraySort:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(1)
    def solution(self):
        minOutOfOrder = float("inf")
        maxOutOfOrder = float("-inf")
        for i in range(len(self.array)):
            num = array[i]
            if self.isOutOfOrder(i, num, array):
                minOutOfOrder = min(minOutOfOrder, num)
                maxOutOfOrder = max(maxOutOfOrder, num)
        
        if minOutOfOrder == float("inf"):
            return [-1, -1]
        
        minSubArrayIdx = 0
        while minOutOfOrder >= self.array[minSubArrayIdx]:
            minSubArrayIdx += 1
        
        maxSubArrayIdx = len(self.array) - 1
        while maxOutOfOrder <= self.array[maxSubArrayIdx]:
            maxSubArrayIdx -= 1
        
        return [minSubArrayIdx, maxSubArrayIdx]
    
    def isOutOfOrder(self, i, num, array):
        if i == 0:
            return num > array[i + 1]
        if i == len(self.array) - 1:
            return num < self.array[i - 1]
        return num < self.array[i - 1] or num > self.array[i + 1]

    
# Testing the solution -
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
array = [1, 2, 3, 4]
array = [1, 2, 5, 4]
obj = SubarraySort(array)
print(obj.solution())       
