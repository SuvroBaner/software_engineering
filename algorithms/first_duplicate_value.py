class FirstDuplicateValue:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(1)
    def solution1(self):
        for i in range(len(self.array)):
            num = abs(array[i])
            idx = num - 1
            search_num = self.array[idx]
            if search_num < 0:
                return num
            else:
                self.array[idx] = self.array[idx] * -1
        return -1

# Testing the solution --

array = [2, 1, 5, 2, 3, 3, 4]
array = [1, 2, 3, 4]
array = [2, 1, 5, 3, 3, 2, 4]
obj = FirstDuplicateValue(array)
print(obj.solution1())