# [MEDIUM] https://leetcode.com/problems/removing-stars-from-a-string
# Completed 2026/03/02
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)