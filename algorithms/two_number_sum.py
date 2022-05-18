class TwoNumberSum:

    def __init__(self, array, targetSum):
        self.array = array
        self.targetSum = targetSum

    # Time : O(n^2) | Space : O(1)
    def solution1(self):
        for i in range(len(self.array)):
            for j in range(i+1, len(self.array)):
                numOne = self.array[i]
                numTwo = self.array[j]
                if (numOne + numTwo) == self.targetSum:
                    return [numOne, numTwo]
        return []

    def solution2(self):
        self.array.sort()
        leftIdx = 0
        rightIdx = len(self.array) - 1
        while leftIdx < rightIdx:
            numOne = self.array[leftIdx]
            numTwo = self.array[rightIdx]
            totalSum = numOne + numTwo
            if totalSum < self.targetSum:
                leftIdx += 1
            elif totalSum > self.targetSum:
                rightIdx -= 1
            else:
                return [numOne, numTwo]
        return []


# Testing the solution -

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
obj = TwoNumberSum(array, targetSum)
print(obj.solution1())
print(obj.solution2())