# Time : O(n) | Space : O(1)
def moveElementToEnd(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        if array[rightIdx] == toMove:
            rightIdx -= 1
        elif array[leftIdx] != toMove:
            leftIdx += 1
        else:
            swap(leftIdx, rightIdx, array)
            leftIdx += 1
            rightIdx -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(array, toMove))