# Time : O(nlogn) | Space : O(1)
def largestRange(array):
    array.sort()
    all_ranges = []
    num = array[0]
    start = num
    max_diff = 0
    result = []

    for i in range(1, len(array)):
        next_integer = num + 1
        if next_integer == array[i] or num == array[i]: # check for same number as well
            end = array[i]
        else:
            end = num
            diff = end - start
            if diff > max_diff:
                max_diff = diff
                result = [start, end]
            start = array[i]
        num = array[i]

    if len(result) == 0:
        return [start, num]
    
    finalDiff = num - start
    lastDiff = result[1] - result[0]
    if finalDiff > lastDiff:
        return [start, num]
    else:
        return result

# Time : O(n) | Space : O(n)
def largestRange(array):
    numHash = {}
    for num in array:
        if num not in numHash:
            numHash[num] = True

    result = []
    max_diff = -1
    for i in range(len(array)):
        num = array[i]
        if not numHash[num]:
            continue
        
        numHash[num] = False
        start = num
        end = num
        
        pre_num = num - 1
        while pre_num in numHash and numHash[pre_num]:
            start = min(start, pre_num)
            numHash[pre_num] = False
            pre_num -= 1
            
        post_num = num + 1
        while post_num in numHash and numHash[post_num]:
            end = max(end, post_num)
            numHash[post_num] = False
            post_num += 1

        diff = end - start
        if diff > max_diff:
            max_diff = diff
            result = [start, end]
        
        start = float("inf")
        end = float("-inf") 
    
    return result

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))

array = [0, 1, 2, 4, 5, 6, 7, 8]
print(largestRange(array))

array = [1, 2, 3, 4]
print(largestRange(array))

array = [1, 3, 5, 7]
print(largestRange(array))

array = [1, 2, 2, 2, 3]
print(largestRange(array))

        
