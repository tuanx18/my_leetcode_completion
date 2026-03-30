# [EASY] https://leetcode.com/problems/clear-digits/
# Completed 2026/03/30
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif ch.isdigit():
                if stack[-1].isdigit():
                    stack.append(ch)
                else:
                    stack.pop()
                    continue
            else:
                stack.append(ch)
        return ''.join(stack)