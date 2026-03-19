# [EASY] https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# Completed 2026/03/17
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ind = 0
        di = 0
        for i in range(1, n + 1):
            if i % m != 0:
                ind += i
            else:
                di += i
        return ind - di