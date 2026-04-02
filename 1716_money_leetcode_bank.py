# [EASY] https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Completed 2026/04/02
class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        curr = 1
        res = 0
        while n > 0:
            res += curr
            curr += 1
            if curr - start == 7:
                start += 1
                curr = start
            n -= 1
        return res