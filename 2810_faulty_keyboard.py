# [EASY] https://leetcode.com/problems/faulty-keyboard
# Completed 2026/04/15
class Solution:
    def finalString(self, s: str) -> str:
        curr = []
        for ch in s:
            if ch == 'i':
                curr.reverse()
                continue
            curr.append(ch)
        return ''.join(curr)