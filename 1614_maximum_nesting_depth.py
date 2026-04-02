# [EASY] https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses
# Completed 2026/03/31
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        ans = 0
        for ch in s:
            if ch == "(":
                depth += 1
            elif ch == ')':
                depth -= 1
            ans = max(ans, depth)
        return ans