# [EASY] https://leetcode.com/problems/number-of-senior-citizens/
# Completed 2026/04/12
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for p in details:
            if int(p[11:13]) > 60:
                res += 1
        return res