class ValidateSubsequence:

    def __init__(self, array, sequence):
        self.array = array
        self.sequence = sequence

    # Time : O(N) where N is the length of array
    # Space : O(1)
    def solution1(self):
        if len(self.sequence) > len(self.array):
            return False

        array_start = 0
        seq_match = 0
        for i in range(len(self.sequence)):
            for j in range(array_start, len(self.array)):
                array_start += 1
                if self.sequence[i] == self.array[j]:
                    seq_match += 1
                    break
            if array_start == len(self.array):
                break
        
        return True if seq_match == len(self.sequence) else False

# Testing the Solution -

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
array = [1, 2, 3, 4]
sequence = []
array = []
sequence = [1]
array = [1, 2, 3, 4]
sequence = [9]
obj = ValidateSubsequence(array, sequence)
print(obj.solution1())