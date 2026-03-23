# https://leetcode.com/problems/count-of-matches-in-tournament/
# Completed 2026/03/23
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            mt = n // 2
            ad = n - mt
            res += mt
            n = ad
        return res