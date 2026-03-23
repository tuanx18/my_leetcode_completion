# [EASY] https://leetcode.com/problems/smallest-even-multiple
# Completed 2026/03/23
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2