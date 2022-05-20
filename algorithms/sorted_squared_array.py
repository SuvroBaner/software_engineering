class SortedSquaredArray:

    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(n)
    def solution1(self):
        result = [0] * len(self.array)
        leftIdx = 0
        rightIdx = len(self.array) - 1
        idx = len(self.array) - 1
        while leftIdx <= rightIdx:
            numOne = self.array[leftIdx] ** 2
            numTwo = self.array[rightIdx] ** 2
            if numTwo >= numOne:
                result[idx] = numTwo
                rightIdx -= 1
            else:
                result[idx] = numOne
                leftIdx += 1
            idx -= 1
        return result

# Testing the solution-

array = [1, 2, 3, 5, 6, 8, 9]
array = [-3, -2, 0, 2, 3, 5]
obj = SortedSquaredArray(array)
print(obj.solution1())