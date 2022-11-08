from typing import List


class Solution:
    # Time : O(num_of_words * max(len(s), len(w)) | Space : O(1)
    # w : word in words list
    def expressiveWords(self, s: str, words = List[str]) -> int:
        total_count = 0
        for w in words:
            i = 0
            j = 0
            stretch = True
            while i < len(s) and j < len(w):
                if s[i] == w[j]:
                    s_count = 1
                    s_idx = i
                    while s_idx < len(s) - 1 and s[s_idx] == s[s_idx + 1]:
                        s_count += 1
                        s_idx += 1
                    
                    w_count = 1
                    w_idx = j
                    while w_idx < len(w) - 1 and w[w_idx] == w[w_idx + 1]:
                        w_count += 1
                        w_idx += 1

                    if s_count >= w_count and (s_count == w_count or s_count >= 3):
                        i = i + s_count
                        j = j + w_count
                    else:
                        stretch = False
                        break
                else:
                    stretch = False
                    break
            if stretch and i == len(s) and j == len(w):
                total_count += 1
        
        return total_count
            
s = "heeellooo"
words = ['hello']
words = ['hello', "hi", "helo"]
s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]
s = 'a'
words = ["aaa"]
s = "abcd"
words = ['abcd']
s = ""
words = [""]
s = "aa"
words = ["a"]
s = "aaa"
words = ["a"]
s = "aaa"
words = ["aaaa"]
s = "a"
words = ["b"]
s = "abcd"
words = ["abc"]
s = "dddiiiinnssssssoooo"
words = ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
#words = ["ddiinnso"]
sol = Solution()
print(sol.expressiveWords(s, words))