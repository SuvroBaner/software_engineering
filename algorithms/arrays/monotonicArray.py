# Time : O(n) | Space : O(1)
def isMonotonic(array):
    left = False
    right = False

    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            left = True
        elif array[i] < array[i+1]:
            right = True
        else:
            pass

        if left and right:
            return False
    return True

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))

array = [1, 2, 3, 0]
print(isMonotonic(array))