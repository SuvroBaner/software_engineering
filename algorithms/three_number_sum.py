class ThreeNumberSum:
    def __init__(self, array, targetSum):
        self.array = array
        self.targetSum = targetSum

    # Time : O(n^2) | Space : O(n)
    def solution1(self):
        self.array.sort()
        result = []
        for i in range(len(self.array)):
            leftIdx = i + 1
            rightIdx = len(self.array) - 1
            while leftIdx < rightIdx:
                numOne = self.array[i]
                numTwo = self.array[leftIdx]
                numThree = self.array[rightIdx]
                if (numOne + numTwo + numThree) < self.targetSum:
                    leftIdx += 1
                elif (numOne + numTwo + numThree) > self.targetSum:
                    rightIdx -= 1
                else:
                    result.append([numOne, numTwo, numThree])
                    leftIdx += 1
                    rightIdx -= 1
        return result

# Testing the solution

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
obj = ThreeNumberSum(array, targetSum)
print(obj.solution1())