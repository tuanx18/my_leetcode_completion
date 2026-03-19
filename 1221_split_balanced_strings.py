# [EASY] https://leetcode.com/problems/split-a-string-in-balanced-strings
# Completed 2026/03/17  
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        res = 0
        for ch in s:
            if ch == "R":
                r += 1
            else:
                l += 1
            
            if r != 0 and r == l:
                r = l = 0
                res += 1
        return res