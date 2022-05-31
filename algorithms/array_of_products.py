class ArrayOfProducts:
    def __init__(self, array):
        self.array = array

    # Time : O(n) | Space : O(n)
    def solution(self):
        prod = 1
        result = [1] * len(self.array)
        for i in range(1, len(self.array)):
            prod = prod * self.array[i-1]
            result[i] = prod

        print(result)
        
        prod = 1
        for i in reversed(range(len(self.array) - 1)):
            prod = prod * self.array[i+1]
            result[i] = result[i] * prod
        
        return result

# Testing the solution -
array = [5, 1, 4, 2]
array = [1, 0, 3, 4]
obj = ArrayOfProducts(array)
print(obj.solution())