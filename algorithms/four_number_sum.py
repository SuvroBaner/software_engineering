class FourNumberSum:
    def __init__(self, array, targetSum):
        self.array = array
        self.targetSum = targetSum

    # Time : O(n^2) | Space : O(n^2)
    def solution(self):
        result = []
        sum_map = {}
        for i in range(1, len(self.array)):
            for j in range(i+1, len(self.array)):
                p1 = self.array[i]
                p2 = self.array[j]
                P = p1 + p2
                Q = self.targetSum - P
                if Q in sum_map:
                    for pair in sum_map[Q]:
                        result.append(pair + [p1, p2])
            for k in range(0, i):
                p1 = self.array[i]
                p2 = self.array[i-k-1]
                P = p1 + p2
                if P not in sum_map:
                    sum_map[P] = [[p1, p2]]
                else:
                    sum_map[P].append([p1, p2])
        return result

# Testing the Solution -
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
obj = FourNumberSum(array, targetSum)
print(obj.solution())

