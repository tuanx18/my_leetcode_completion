# [EASY] https://leetcode.com/problems/replace-all-digits-with-characters
# Completed 2026/04/01
class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char, k):
            new = chr(ord(char) + k)
            return new
        
        res = ''
        for i in range(len(s)):
            if s[i].isdigit():
                new_ch = shift(s[i-1], int(s[i]))
                res += new_ch
            else:
                res += s[i]
        return res