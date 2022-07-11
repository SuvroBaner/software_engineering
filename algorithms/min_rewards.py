class minRewards:
    def __init__(self, scores):
        self.scores = scores

    # Time : O(n^2) | Space : O(n)
    def solution1(self):
        rewards = [1 for _ in self.scores]
        for i in range(1, len(self.scores)):
            j = i - 1
            if self.scores[i] > self.scores[j]:
                rewards[i] = rewards[j] + 1
            else:
                while j >= 0 and self.scores[j] > self.scores[j + 1]:
                    rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                    j -= 1
        return sum(rewards)

    # Time : O(n) | Space : O(n)
    def solution2(self):
        rewards = [1 for _ in self.scores]
        localMinIdxs = self.getLocalMinIdxs(self.scores)
        for localMinIdx in localMinIdxs:
            self.expandFromLocalMinIdx(localMinIdx, rewards)
        return sum(rewards)

    def getLocalMinIdxs(self, array):
        if len(array) == 1:
            return [0]
        localMinIdxs = []
        for i in range(len(array)):
            if i == 0 and array[i] < array[i + 1]:
                localMinIdxs.append(i)
            if i == len(array) - 1 and array[i] < array[i - 1]:
                localMinIdxs.append(i)
            if i == 0 or i == len(array) -1 :
                continue
            if array[i] < array[i - 1] and array[i] < array[i + 1]:
                localMinIdxs.append(i)
        return localMinIdxs

    def expandFromLocalMinIdx(self, localMinIdx, rewards):
        leftIdx = localMinIdx - 1
        while leftIdx >= 0 and self.scores[leftIdx] > self.scores[leftIdx + 1]:
            rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
            leftIdx -= 1
        rightIdx = localMinIdx + 1
        while rightIdx <= len(self.scores) - 1 and self.scores[rightIdx] > self.scores[rightIdx - 1]:
            rewards[rightIdx] = rewards[rightIdx - 1] + 1
            rightIdx += 1
        return rewards

    # Time : O(n) | Space : O(n)
    def solution3(self):
        rewards = [1 for _ in self.scores]
        for i in range(1, len(self.scores)):
            if self.scores[i] > self.scores[i - 1]:
                rewards[i] = rewards[i - 1] + 1
        for i in reversed(range(len(self.scores) - 1)):
            if self.scores[i] > self.scores[i + 1]:
                rewards[i] = max(rewards[i], rewards[i + 1] + 1)
        return sum(rewards)


# Testing the solution -
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
obj = minRewards(scores)
print(obj.solution1())
print(obj.solution2())
print(obj.solution3())