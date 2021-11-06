# Time : O(n) | Space : O(1)
def longestPeak(array):
    hasPeak = False
    longestPeak = float("-inf")
    for i in range(1, len(array) - 1):
        peakSize = 3
        if array[i] > array[i-1] and array[i] > array[i+1]:
            hasPeak = True
            leftIdx = i - 1
            while leftIdx > 0 and array[leftIdx] > array[leftIdx - 1]:
                peakSize += 1
                leftIdx -= 1
            
            rightIdx = i + 1
            while rightIdx < len(array) - 1 and array[rightIdx] > array[rightIdx + 1]:
                peakSize += 1
                rightIdx += 1
        
        longestPeak = max(longestPeak, peakSize)
    
    return longestPeak if hasPeak else 0

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))
            
