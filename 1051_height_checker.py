# [EASY] https://leetcode.com/problems/height-checker/
# Completed 2026/04/05
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = heights[:]
        exp.sort()
        res = 0
        for i in range(len(exp)):
            if exp[i] != heights[i]:
                res += 1
        return res