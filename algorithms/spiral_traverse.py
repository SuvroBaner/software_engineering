class SpiralTraverse:
    def __init__(self, array):
        self.array = array

    # Time : O(n) where n is the number of elements in the array
    # Space : O(n)
    def solution(self):
        startRow = 0
        startCol = 0
        endRow = len(self.array) - 1
        endCol = len(self.array[0]) - 1
        result = []

        while startRow <= endRow and startCol <= endCol:
            for col in range(startCol, endCol + 1):
                result.append(self.array[startRow][col])
            
            for row in range(startRow + 1, endRow + 1):
                result.append(self.array[row][endCol])
            
            for col in reversed(range(startCol, endCol)):
                if startRow == endRow:
                    continue
                result.append(self.array[endRow][col])
            
            for row in reversed(range(startRow + 1, endRow)):
                if startCol == endCol:
                    continue
                result.append(self.array[row][startCol])
            
            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1

        return result

# Testing the solution -

array = [
    [1, 2, 3, 4], 
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

array = [
    [1, 2, 3],
    [10, 11, 4],
    [9, 12, 5],
    [8, 7, 6]
]

obj = SpiralTraverse(array)
print(obj.solution())
        