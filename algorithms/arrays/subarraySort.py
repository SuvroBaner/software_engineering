def subarraySort(array):
    first = True
    sorting = False
    largest = max(array[0], array[1])
    smallestIdx = float("inf")
    largestIdx = float("-inf")

    for i in range(len(array) - 1):
        if array[i] > array[i+1] or array[i+1] < largest:
            sorting = True
            unsortedIdx = i+1
            if first:
                startIdx = i-1
                first = False
            
            while startIdx >=0 and array[startIdx] > array[unsortedIdx]:
                startIdx -= 1
            
            smallestIdx = min(smallestIdx, startIdx+1)
            largestIdx = max(largestIdx, unsortedIdx)
        
        largest = max(largest, array[i+1])
    
    return [smallestIdx, largestIdx] if sorting else [-1, -1]

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))

array = [8, 6, 4, 2, 1]
print(subarraySort(array))
