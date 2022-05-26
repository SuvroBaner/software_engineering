class SmallestDifference:
    def __init__(self, arrayOne, arrayTwo):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo

    # Time : O(nlogn + mlogm) where n is the length of arrayOne and m is the length of arrayTwo
    def solution1(self):
        self.arrayOne.sort()
        self.arrayTwo.sort()
        smallest = float("inf")
        arrayOneIdx = 0
        arrayTwoIdx = 0
        smallestPair = []
        while arrayOneIdx < len(self.arrayOne) and arrayTwoIdx < len(self.arrayTwo):
            numOne = self.arrayOne[arrayOneIdx]
            numTwo = self.arrayTwo[arrayTwoIdx]
            diff = abs(numOne - numTwo)
            if diff < smallest:
                smallest = diff
                smallestPair = [numOne, numTwo]
            
            if numOne < numTwo:
                arrayOneIdx += 1
            elif numOne > numTwo:
                arrayTwoIdx += 1
            else:
                return [numOne, numTwo]
        
        return smallestPair

# Testing out the solution -

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
#arrayTwo = [26, 27, 134, 135, 15, 17]
obj = SmallestDifference(arrayOne, arrayTwo)
print(obj.solution1())
                    