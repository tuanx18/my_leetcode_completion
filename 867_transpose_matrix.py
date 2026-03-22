# [EASY] https://leetcode.com/problems/transpose-matrix
# Completed 2026/03/22
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        trans = list(zip(*matrix))
        trans = [list(row) for row in trans]
        return trans