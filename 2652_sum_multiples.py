# [EASY] https://leetcode.com/problems/sum-multiples/
# Completed 2026/03/18
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
        return res