# Time : O(n) | Space : O(n)
def spiralTraverse(array):
    result = []

    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        if startRow == endRow:
            break

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])


        if startCol == endCol:
            break

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result

array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

print(spiralTraverse(array))

array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

print(spiralTraverse(array))

array = [
    [1, 2, 3],
    [10, 11, 4],
    [9, 12, 5],
    [8, 7, 6]
]

print(spiralTraverse(array))