# Time : O(n^2) | Space : O(n)
def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1] + 1)
                j -= 1
    return sum(rewards)

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))

# Time : O(n) | Space : O(n)
def minRewards(scores):
    rewards = [1 for _ in scores]
    minIndxs = getAllMinIndxs(scores)
    for minIndx in minIndxs:
        i = minIndx - 1
        while i >= 0 and scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)
            i -= 1
        
        j = minIndx + 1
        while j < len(scores) and scores[j] > scores[j-1]:
            rewards[j] = rewards[j-1] + 1
            j += 1
    return sum(rewards)

def getAllMinIndxs(array):
    minIndxs = []
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [0]
    if len(array) == 2:
        if array[0] < array[1]:
            return [0]
        else:
            return [1]
    for i in range(1, len(array)-1):
        if i == 1 and array[i-1] < array[i]:
            minIndxs.append(i-1)
        if array[i] < array[i+1] and array[i] < array[i-1]:
            minIndxs.append(i)
        if i == len(array) - 2 and array[i+1] < array[i]:
            minIndxs.append(i+1)
        
    return minIndxs

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))

# Time : O(n) | Space : O(n)
def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
    for i in reversed(range(len(scores) - 1)):
        j = i + 1
        if scores[i] > scores[j]:
            rewards[i] = max(rewards[i], rewards[j] + 1)
    
    return sum(rewards)

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))
