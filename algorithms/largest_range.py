class LargestRange:
    def __init__(self, array):
        self.array = array

    # Time : O(nlogn) | Space : O(n)
    def solution1(self):
        self.array.sort()
        results = []
        start = self.array[0]
        end = self.array[0]
        for i in range(1, len(self.array)):
            num = self.array[i]
            prev_num = self.array[i - 1]
            if (num == prev_num + 1) or (num == prev_num):
                end = num
            else:
                if start != end:
                    results.append([start, end])
                
                start = num
                end = num
        if start != end:
            results.append([start, end])
        
        largest = 0
        out = []
        for result in results:
            diff = result[1] - result[0]
            if diff > largest:
                largest = diff
                out = result
        return [start, end] if len(self.array) == 1 else out


# Testing the solution -
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
#array = [0, 4, 5, 6]
#array = [0, 3, 5, 6, 7, 9]
array = [1]
array = [0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
#array = [1, 2, 3, 3, 4, 5]
obj = LargestRange(array)
print(obj.solution1())