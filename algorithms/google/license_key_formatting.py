class Solution:
    # Time : O(n) | Space : O(n)
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        count = 0
        s = s.replace("-", "")
        for i in reversed(range(len(s))):
            result.append(s[i].upper())
            count += 1
            # we don't want to put a dash in the first position of the array, so i != 0
            if count == k and i != 0:
                result.append("-")
                count = 0
        return ''.join(result[::-1]) # doing a reverse
        
        

s = "5F3Z-2e-9-w" ; k = 4
s = "2-5g-3-J" ; k = 2
sol = Solution()
print(sol.licenseKeyFormatting(s, k))