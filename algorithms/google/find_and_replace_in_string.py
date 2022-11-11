from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        result = list(s)
        for i in range(len(sources)):
            source = sources[i]
            source_len = len(source)
            indx = indices[i]
            target = targets[i]

            if not s[indx: ].startswith(source):
                continue
            result[indx] = target
            for j in range(indx + 1, indx + source_len):
                result[j] = ''
        
        return "".join(result)
        

s = "abcd"
indices = [0, 2]
sources = ["ab", "cd"]
targets = ["eee", "ffff"]

# s = "abcd"
# indices = [0, 2]
# sources = ["ab","ec"]
# targets = ["eee","ffff"]

# s = "vmokgggqzp"
# indices = [3,5,1]
# sources = ["kg","ggg","mo"]
# targets = ["s","so","bfr"]

sol = Solution()
print(sol.findReplaceString(s, indices, sources, targets))
