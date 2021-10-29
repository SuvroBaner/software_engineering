# Time : O(n)
# Space : O(1)

def isValidSubsequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
    while arrayIdx <= len(array) - 1 and seqIdx <= len(sequence) - 1:
        if array[arrayIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrayIdx += 1

    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

array = [5, 1, 4, 6, 8, 10]
sequence = [1, 6]

array = [5, 1, 4, 6]
sequence = [6, 1]

array = [1, 2, 3, 4]
sequence = []

array = [1]
sequence = []

print(isValidSubsequence(array, sequence))