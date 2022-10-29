class Solution:
    # Time : O(n) | Space : O(1) or O(m)
    # where 'm' is the unique characters 
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        char_idx_map = {}

        while end < len(s):
            ch = s[end]
            if ch in char_idx_map:
                prev_ch_idx = char_idx_map[ch]    
                if prev_ch_idx >= start:
                    start = prev_ch_idx + 1
            
            char_idx_map[ch] = end
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
        

s = "abc"
s = ""
s = "abcpqrst"
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))