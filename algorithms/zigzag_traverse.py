class zigZagTraverse:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(n)
    # where n = num of elements in the array
    def solution1(self):
        rows = len(self.array)
        cols = len(self.array[0])
        n = rows * cols
        row = 0
        col = 0
        result = []
        direction = 'down'
        count = 0

        while count < n:
            count += 1
            result.append(self.array[row][col])

            if row + 1 < rows and col == 0 and direction == 'down':
                # not the last row AND first column AND direction is down (also the initial cond)
                # then go down 
                row += 1
                direction = 'up'
            
            elif row > 0 and col + 1 < cols and direction == 'up':
                # not the first row AND not the last column AND direction is up
                # then go up (diagonally)
                row -= 1
                col += 1

            elif row == 0 and col + 1 < cols and direction == 'up':
                # first row AND not the last column AND direction is up
                # then go up (horizontally)
                col += 1
                direction = 'down'

            elif col > 0 and row + 1 < rows and direction == 'down':
                # not the first column AND not the last row AND direction is down
                # then go down (diagonally)
                row += 1
                col -= 1

            elif row + 1 < rows and col + 1 == cols and direction == 'up':
                # not the last row AND last column AND direction is up
                # then go down (straight)
                row += 1
                direction = 'down'

            elif row + 1 == rows and col + 1 < cols and direction == 'down':
                # last row AND not the last column AND direction is down
                # then go up (horizontally)
                col += 1
                direction = 'up'

        return result

# --- Testing the solution  -

array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
]

obj = zigZagTraverse(array)
print(obj.solution1())