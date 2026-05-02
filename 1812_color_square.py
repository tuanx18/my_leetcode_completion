# [EASY] https://leetcode.com/problems/determine-color-of-a-chessboard-square
# Completed 2026/01/05
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord("h") - ord(coordinates[0])
        val = int(coordinates[1]) - col
        if val % 2 == 0:
            return False
        return True