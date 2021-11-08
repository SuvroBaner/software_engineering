# Time : O(n) | Space : O(1)
def firstDuplicateValue(array):
    n = len(array)
    found = False
    for i in range(n):
        idxToCheck = n - abs(array[i])
        if array[idxToCheck] < 0:
            found = True
            break
        else:
            array[idxToCheck] = array[idxToCheck] * -1
    return abs(array[i]) if found else -1 

array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))

array = [2, 1, 5, 3, 3, 2, 4]
print(firstDuplicateValue(array))

array = [1, 2, 3, 4]
print(firstDuplicateValue(array))

array = []
print(firstDuplicateValue(array))