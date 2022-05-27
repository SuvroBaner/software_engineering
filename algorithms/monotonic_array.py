class MonotonicArray:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(1)
    def solution(self):
        direction = {'increasing': False, 'decreasing': False}
        for i in range(len(self.array) - 1):
            first = self.array[i]
            second = self.array[i+1]
            if second > first:
                direction['increasing'] = True
            elif second < first:
                direction['decreasing'] = True
            else:
                pass

            if direction['increasing'] and direction['decreasing']:
                return False
        return True

# Testing the solution -
array = [-1, -2, -3, -3, -5]
array = [1, 2, 3, 4, 5]
array = [1, 2, 3, 1, 9]
array = [1, 1, 1, 1, 1, 12]
array = [1, 1, 1, 1, 1, 1]
array = [1]
array = []

obj = MonotonicArray(array)
print(obj.solution())
