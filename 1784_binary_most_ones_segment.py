# [EASY] https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones
# Completed 2026/03/26
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cons = True
        for i in range(len(s)):
            if s[i] == '0' and cons:
                cons = False
            if s[i] == '1' and not cons:
                return False
        return True