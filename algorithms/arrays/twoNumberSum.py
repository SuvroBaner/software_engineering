# Time : O(nlogn) | Space : O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        numberOne = array[leftIdx]
        numberTwo = array[rightIdx]
        calcSum = numberOne + numberTwo
        if calcSum < targetSum:
            leftIdx += 1
        elif calcSum > targetSum:
            rightIdx -= 1
        else:
            return [numberOne, numberTwo]
    return []

# Time : O(n) | Space : O(n)
def twoNumberSum(array, targetSum):
    numberSerach = {}
    for num in array:
        numberSerach[num] = True
    
    for num in array:
        numberSerach[num] = False
        prospectNum = targetSum - num
        if prospectNum in numberSerach and numberSerach[prospectNum]:
            return [num, prospectNum]
    return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
#array = [3, 5, -4, 8, 11, 1, -1, 6]
#targetSum = 100
print(twoNumberSum(array, targetSum))