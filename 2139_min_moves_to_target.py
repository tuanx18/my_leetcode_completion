# [MEDIUM] https://leetcode.com/problems/minimum-moves-to-reach-target-score/
# Completed 2026/03/18
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num = target
        step = 0
        while num > 1:
            if num % 2 == 0 and maxDoubles > 0:
                num //= 2
                maxDoubles -= 1
            elif maxDoubles == 0:
                step += num - 1
                break
            else:
                num -= 1
            step += 1
        return step