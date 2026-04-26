# [EASY] https://leetcode.com/problems/furthest-point-from-origin
# Completed 2026/04/24
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count("L")
        R = moves.count("R")
        blank = moves.count("_")

        return abs(R - L) + blank