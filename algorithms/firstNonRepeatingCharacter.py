from itertools import count


class firstNonRepeatingCharacter:
    def __init__(self, string):
        self.string = string

    # Time : O(n) | Space : O(1) as it has only 26 letter in the alphabet
    def solution(self):
        char_dict = {}
        for idx in range(len(self.string)):
            ch = self.string[idx]
            if ch not in char_dict:
                char_dict[ch] = [idx, 1]
            else:
                char_dict[ch][1] += 1
        
        minIdx = float("inf")
        for k,v in char_dict.items():
            _idx = v[0]
            _count = v[1]
            if _count > 1:
                continue
            if _idx < minIdx:
                minIdx = _idx
        
        return minIdx if minIdx != float("inf") else -1

# -- Testing the solution -
string = "abcdcaf"
obj = firstNonRepeatingCharacter(string)
print(obj.solution())