class Solution:
    # Time : O(n) | Space : O(n)
    # 'n' : length of the maximum string 's' or 't
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = self.parseString(s)
        new_t = self.parseString(t)
        
        print(new_s, new_t)
        
        return True if new_s == new_t else False
    
    def parseString(self, x: str) -> str:
        new_x = list(x)
        j = 0
        for i in range(len(x)):
            if x[i] != '#':
                new_x[j] = x[i]
                j += 1
            else:
                if j > 0:
                    j -= 1
        return ''.join(new_x[0:j])
    
s = "ab#c"
t = "ad#c"

# s = "ab##"
# t = "c#d#"

# s = "a#c"
# t = "b"

# s = ''
# t = '####'

s = "y#fo##f"
t = "y#f#o##f"

sol = Solution()
print(sol.backspaceCompare(s, t))