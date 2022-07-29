# Time : O(n * m) | Space : O(n * m)
def globMatching(filename, pattern):
    matchTable = initializeMatchTable(filename, pattern)
    
    for i in range(1, len(filename) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == "*":
                matchTable[i][j] = matchTable[i][j - 1] or matchTable[i - 1][j]
            elif pattern[j - 1] == "?" or filename[i - 1] == pattern[j - 1]:
                matchTable[i][j] = matchTable[i - 1][j - 1]
            else:
                matchTable[i][j] = False
    return matchTable[len(filename)][len(pattern)]
    
    
def initializeMatchTable(filename, pattern):
    matchTable = [[False for j in range(len(pattern) + 1)] for i in range(len(filename) + 1)]
    
    matchTable[0][0] = True
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == "*":
            matchTable[0][j] = matchTable[0][j - 1]
    
    return matchTable

filename = "albmnc"
pattern = "a?b*c"
print(globMatching(filename, pattern))

    