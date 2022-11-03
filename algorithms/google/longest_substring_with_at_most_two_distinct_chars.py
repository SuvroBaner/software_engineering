class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 1:
            return 1
        two_chars = {}
        start = 0
        result = [-1, -1]
        longest = float("-inf")
        
        for i in range(len(s)):
            ch = s[i]
            two_chars[ch] = 1 + two_chars.get(ch, 0)
            distinct_chars = len(two_chars)
            
            if distinct_chars > 2:
                substring_len = i - start
                if substring_len > longest:
                    longest = substring_len
                    result = [start, i - 1]
            
            while distinct_chars > 2:
                pop_char = s[start]
                two_chars[pop_char] -= 1
                if two_chars[pop_char] == 0:
                    del two_chars[pop_char]
                
                distinct_chars = len(two_chars)
                start += 1
        
        if (i - start) > (result[1] - result[0]):
            start_idx = start
            end_idx = i
        else:
            start_idx = result[0]
            end_idx = result[1]

        return len(s[start_idx : end_idx + 1])

s = 'eceba'
s = "ccaabbb"
s = "a"
sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct(s))