# Time : O(n^2) | Space : O(n^2)
def fourNumberSum(array, targetSum):
    firstPairSum = {}
    result = []
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            num1 = array[i]
            num2 = array[j]
            secondPairSum = num1 + num2
            diff = targetSum - secondPairSum
            if diff in firstPairSum:
                for pair in firstPairSum[diff]:
                    result.append(pair + [num1, num2])

        for k in range(0, i):
            pairSum = array[k] + array[i]
            if pairSum not in firstPairSum:
                firstPairSum[pairSum] = [[array[k], array[i]]]
            else:
                firstPairSum[pairSum].append([array[k], array[i]])
    
    return result
   

array = [7, 6, 4, -1, 1, 2]
targetSum = 16
print(fourNumberSum(array, targetSum))

array = [1, 2, 3, 4, 5, 6, 7]
targetSum = 10
print(fourNumberSum(array, targetSum))
