class levenshteinDistance:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    # Time : O(nm) | Space : O(nm)
    # where n, m are the length of the str1 and str2 respectively
    def solution(self):
        edit = [[0 for j in range(len(self.str2) + 1)] for i in range(len(self.str1) + 1)]
        for i in range(len(self.str2) + 1):
            edit[0][i] = i
        for i in range(len(self.str1) + 1):
            edit[i][0] = i

        for r in range(1, len(self.str1) + 1):
            for c in range(1, len(self.str2) + 1):
                if self.str1[r - 1] == self.str2[c - 1]:
                    edit[r][c] = edit[r - 1][c - 1]
                else:
                    edit[r][c] = 1 + min(edit[r - 1][c - 1], edit[r][c - 1], edit[r - 1][c])
        return edit[len(str1)][len(str2)]

# -- testing the solution -
str1 = "abc"
str2 = "yabd"
obj = levenshteinDistance(str1, str2)
print(obj.solution())


