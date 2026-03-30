# [EASY] https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits
# Completed 2026/03/30
class Solution:
    def minimumSum(self, num: int) -> int:
        digit = []
        for ch in str(num):
            digit.append(ch)
        digit.sort()
        n1 = (digit[0] + digit[2]).lstrip('0')
        n2 = (digit[1] + digit[3]).lstrip('0')
        if len(n1) == 0:
            n1 = 0
        if len(n2) == 0:
            n2 = 0
        return int(n1) + int(n2)