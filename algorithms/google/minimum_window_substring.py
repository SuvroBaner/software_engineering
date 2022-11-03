# class Solution:
#     # Time : O(n * n) - Worst
#     # Time : O(n * m) - Average
#     # Space : O(1)
#     def minWindow(self, s: str, t: str) -> str:
#         target_map = {}
#         for target in t:
#             if target not in target_map:
#                 target_map[target] = 1
#             else:
#                 target_map[target] += 1
        
#         target_idx = []
#         for i in range(len(s)):
#             if s[i] in target_map:
#                 target_idx.append(i)
        
#         min_window_start_idx = -1
#         min_window_end_idx = -1
#         min_window = float("inf")
#         for idx in target_idx:
#             window_size = 0
#             start = idx
#             search = True
#             search_target_map = target_map.copy() # shallow copy
#             while start < len(s) and search:
#                 window_size += 1
#                 if s[start] in search_target_map:
#                     search_target_map[s[start]] -= 1
#                     for _, v in search_target_map.items():
#                         if v > 0:
#                             search = True
#                             break
#                         else:
#                             search = False
#                 if not search:
#                     if window_size < min_window:
#                         min_window = window_size
#                         min_window_start_idx = idx
#                         min_window_end_idx = start
#                 start += 1
#         if min_window_start_idx == -1:
#             return ""
#         else:
#             return s[min_window_start_idx: min_window_end_idx + 1]

# class Solution:
#     # Time : O(n) | Space : O(1)
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "": return ""

#         countT, window = {}, {}

#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)

#         have, need = 0, len(countT)
#         res, resLen = [-1, -1], float("inf")
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1

#             while have == need:
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = (r - l + 1)
                
#                 window[s[l]] -= 1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1
#         l, r = res
#         return s[l : r + 1] if resLen != float("inf") else ""


from itertools import count


class Solution:
    # Time : O(n) | Space : O(1)
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        have = 0
        need = len(countT)
        start = 0
        result = [-1, -1]
        min_len = float("inf")
        for end in range(len(s)):
            ch = s[end]
            if ch in countT:
                window[ch] = 1 + window.get(ch, 0)
                if window[ch] == countT[ch]:
                    have += 1
            while have == need:
                window_size = end - start + 1
                if window_size < min_len:
                    min_len = window_size
                    result = [start, end]
                if s[start] in countT:
                    if window[s[start]] <= countT[s[start]]:
                        have -= 1
                    window[s[start]] -= 1
                start += 1
        start, end = result[0], result[1]
        return s[start : end + 1] if min_len != float("inf") else ""

s = "ADPQCBNART"
t = "ABC"
s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"
s = "a"
t = "aa"
s = "cabwefgewcwaefgcf"
t = "cae"
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
sol = Solution()
print(sol.minWindow(s, t))