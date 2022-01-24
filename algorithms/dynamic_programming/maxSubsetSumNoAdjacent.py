# Time : O(n) | Space : O(n)
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array[0], array[1])
    else:
        result = [0]*len(array)
        result[0] = array[0]
        result[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        newSum = max(result[i-1], result[i-2] + array[i])
        result[i] = newSum

    return result[-1]

array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))

# Let's imporve the space complexity

# Time : O(n) | Space : O(1)
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, array[i] + second)
        second = first
        first = current

    return first

array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))