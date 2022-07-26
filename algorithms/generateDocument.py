class generateDocument:
    def __init__(self, characters, document):
        self.characters = characters
        self.document = document

    # Time : O(d + c) where d is the number of characters in documents and
    # c : number of characters in characters
    # Space : O(c)
    def solution(self):
        char_dict = {}
        for ch in self.characters:
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1
        
        for doc in self.document:
            if doc not in char_dict:
                return False
            if char_dict[doc] == 0:
                return False
            char_dict[doc] -= 1
        return True

#--- Testing the Solution - 
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
characters = ""
document = ""
obj = generateDocument(characters, document)
print(obj.solution())
        
    