from numpy import array


class MoveElementToEnd:
    def __init__(self, array, toMove):
        self.array = array
        self.toMove = toMove

    # Time : O(n) | Space : O(1)
    def solution(self):
        leftIdx = 0
        rightIdx = len(self.array) - 1
        while leftIdx < rightIdx:
            if self.array[rightIdx] == self.toMove:
                rightIdx -= 1
            elif self.array[leftIdx] == self.toMove:
                self.swap(leftIdx, rightIdx)
                leftIdx += 1
                rightIdx -= 1
            else:
                leftIdx += 1
        return self.array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

# Test the solution -

ip_array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
obj = MoveElementToEnd(ip_array, toMove)
print(obj.solution())
        