# [EASY] https://leetcode.com/problems/rotate-string
# Completed 2026/05/03
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        L = len(s)
        x = 0
        while x < L:
            if s == goal:
                return True
            s = s[1:] + s[0]
            x += 1
        return False