# Time : O(nlog(n) + mlog(m)) | Space : O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    oneIdx = 0
    twoIdx = 0
    smallest = float("inf")
    result = []
    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        numberOne = arrayOne[oneIdx]
        numberTwo = arrayTwo[twoIdx]
        difference = numberOne - numberTwo

        if abs(difference) < smallest:
            smallest = abs(difference)
            result = [numberOne, numberTwo]

        if difference < 0:
            oneIdx += 1
        elif difference > 0:
            twoIdx += 1
        else:
            return [numberOne, numberTwo]
    
    return result

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne, arrayTwo))