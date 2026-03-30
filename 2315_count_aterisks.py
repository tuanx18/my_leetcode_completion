# [EASY] https://leetcode.com/problems/count-asterisks/
# Completed 2026/03/30
class Solution:
    def countAsterisks(self, s: str) -> int:
        parts = s.split("|")
        res = 0
        for i in range(0, len(parts), 2):
            res += parts[i].count("*")
        return res