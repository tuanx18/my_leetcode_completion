# [EASY] https://leetcode.com/problems/maximum-odd-binary-number/
# Completed 2026/04/08
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zr = s.count('0')
        oe = s.count('1')

        return '1' * (oe - 1) + '0' * zr + '1'