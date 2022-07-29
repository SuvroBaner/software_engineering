def longestStreakOfAdjacentOnes(array):
    zerosIdx = []
    for i in range(len(array)):
        if array[i] == 0:
            zerosIdx.append(i)
    
    if len(zerosIdx) == 0:
        return -1
            
    max_ones = []
    for idx in zerosIdx:
        leftIdx = idx - 1
        count = 1
        while leftIdx >= 0 and array[leftIdx] == 1:
            count += 1
            leftIdx -= 1
        rightIdx = idx + 1
        while rightIdx <= len(array) - 1 and array[rightIdx] == 1:
            count += 1
            rightIdx += 1
        max_ones.append(count)
        
    largest = float("-inf")
    final_idx = -1
    for i in range(len(max_ones)):
        if max_ones[i] > largest:
            largest = max_ones[i]
            final_idx = i
    
    return zerosIdx[final_idx]

array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
#array = [1, 1, 1, 1, 1]
print(longestStreakOfAdjacentOnes(array))