class caesarCipherEncryptor:
    def __init__(self, string, key):
        self.string = string
        self.key = key

    # Time : O(n) | Space : O(n)
    def solution(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = []
        for ch in self.string:
            pos = alphabet.index(ch)
            new_pos = (pos + self.key) % 26
            result.append(alphabet[new_pos])
        return "".join(result)

# --- Testing the solution -
string = 'xyz'
key = 2
obj = caesarCipherEncryptor(string, key)
print(obj.solution())
