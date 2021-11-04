# Time : O(n^2) | Space : O(n)
def threeNumberSum(array, targetSum):
    result = []
    array.sort()

    for i in range(len(array)):
        firstNumber = array[i]
        leftIdx = i+1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            secondNumber = array[leftIdx]
            thirdNumber = array[rightIdx]
            totalSum = firstNumber + secondNumber + thirdNumber
            if totalSum < targetSum:
                leftIdx += 1
            elif totalSum > targetSum:
                rightIdx -= 1
            else:
                result.append([firstNumber, secondNumber, thirdNumber])
                leftIdx += 1
                rightIdx -= 1
    return result

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))