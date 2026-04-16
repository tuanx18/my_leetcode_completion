# [EASY] https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Completed 2026/04/15
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        trns = list(zip(*matrix))
        trns = [list(x) for x in trns]

        res = []

        for i in trns:
            res.append(sum(i))
        
        return res