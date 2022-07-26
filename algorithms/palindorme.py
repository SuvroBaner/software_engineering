import string


class isPalindrome:
    def __init__(self, string):
        self.string = string

    # Time : O(n) | Space : O(1)
    def solution(self):
        leftIdx = 0
        rightIdx = len(self.string) - 1
        while leftIdx < rightIdx:
            if self.string[leftIdx] != self.string[rightIdx]:
                return False
            leftIdx += 1
            rightIdx -= 1
        return True

#Testing the solution -
_string = "abc"
_string = 'madam'
obj = isPalindrome(_string)
print(obj.solution())