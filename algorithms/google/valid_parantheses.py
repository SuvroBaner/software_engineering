class Solution:
    # Time : O(n) | Space : O(n)
    # where n is the length of the string
    def isValid(self, s: str) -> bool:
        char_map = {'(': ')', '{': '}', '[': ']'}
        char_stack = []
        for i in range(len(s)):
            chr = s[i]
            if chr in char_map:
                char_stack.append(chr)
            else:
                if not char_stack:
                    return False
                prev_char = char_stack.pop()
                if char_map[prev_char] != chr:
                    return False
        if char_stack:
            return False
        
        return True

s = "((){[()]})"
s = "((("
s = ")))"
s = ")()"
s = "(]"
s = "()"
s = "()[]{}"
sol = Solution()
print(sol.isValid(s))
print("This is my new commit")