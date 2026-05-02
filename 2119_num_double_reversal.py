# [EASY] https://leetcode.com/problems/a-number-after-a-double-reversal/
# Completed 2026/04/30
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True