class maxSubsetSumNoAdjacent:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(n)
    def solution(self):
        if len(self.array) == 0:
            return 0
        if len(self.array) == 1:
            return self.array[0]
        if len(self.array) == 2:
            return max(self.array[0], self.array[1])

        max_sum_array = [0] * len(self.array)
        max_sum_array[0] = self.array[0]
        max_sum_array[1] = max(self.array[0], self.array[1])
        for i in range(2, len(self.array)):
            maxSum = max(max_sum_array[i-1], max_sum_array[i-2] + self.array[i])
            max_sum_array[i] = maxSum
        return max_sum_array[-1]

    # Time : O(n) | Space : O(1)
    def solution2(self):
        if len(self.array) == 0:
            return 0
        if len(self.array) == 1:
            return self.array[0]
        if len(self.array) == 2:
            return max(self.array[0], self.array[1])

        first = self.array[0]
        second = max(self.array[0], self.array[1])
        for i in range(2, len(self.array)):
            maxSum = max(second, first + self.array[i])
            first = second
            second = maxSum
        return second


# -- Testing the solution
array = [7, 10, 12, 7, 9, 14]
array = []
array = [6, 19]
array = [19, 6]
array = [4, 3, 5, 200, 5, 3]
array = [2]
obj = maxSubsetSumNoAdjacent(array)
print(obj.solution())
print(obj.solution2())