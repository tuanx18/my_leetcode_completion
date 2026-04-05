# [EASY] https://leetcode.com/problems/robot-return-to-origin
# Completed 2026/04/05
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hor = 0
        ver = 0
        for ch in moves:
            if ch == "L":
                hor -= 1
            elif ch == "R":
                hor += 1
            elif ch == "U":
                ver += 1
            else:
                ver -= 1
        if hor == 0 and ver == 0:
            return True
        else:
            return False