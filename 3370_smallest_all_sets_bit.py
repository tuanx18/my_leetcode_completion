# [EASY] https://leetcode.com/problems/smallest-number-with-all-set-bits/
# Completed 2026/04/12
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << len(bin(n)[2:])) - 1