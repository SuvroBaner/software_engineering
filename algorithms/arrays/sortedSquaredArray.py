# Time : O(n) | Space : O(n)

def sortedSquaredArray(array):
    squaredArray = [0]*len(array)
    leftIdx = 0
    rightIdx = len(array) - 1
    newIdx = len(squaredArray) - 1

    while leftIdx <= rightIdx:
        if abs(array[leftIdx]) >= abs(array[rightIdx]):
            squaredArray[newIdx] = array[leftIdx] ** 2
            leftIdx += 1
        else:
            squaredArray[newIdx] = array[rightIdx] ** 2
            rightIdx -= 1
        
        newIdx -= 1 

    return squaredArray

array = [1, 2, 3, 5]
print(sortedSquaredArray(array))

array = [-2, 0, 1, 2]
print(sortedSquaredArray(array))

array = [-5, 0, 1, 2]
print(sortedSquaredArray(array))

array = [-5, -1, 0, 1, 2]
print(sortedSquaredArray(array))
