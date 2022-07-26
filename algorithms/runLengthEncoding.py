class runLengthEncoding:
    def __init__(self, string):
        self.string = string

    # Time : O(n) | Space : O(n)
    def solution(self):
        letter = self.string[0]
        count = 1
        result = []
        for i in range(1, len(self.string)):
            new_letter = self.string[i]
            if letter == new_letter:
                if count == 9:
                    result.append(str(count) + letter)
                    count = 0
                count += 1
            else:
                element = str(count) + letter
                result.append(element)
                letter = new_letter
                count = 1
        return "".join(result) + str(count) + letter

# -- Testing the solution -
string = "AAAA"
string = "AAAABB"
string = "AAAAAAAAAAAAABBCCCCDD"
obj = runLengthEncoding(string)
print(obj.solution())