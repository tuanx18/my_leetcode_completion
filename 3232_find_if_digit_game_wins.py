# [EASY] https://leetcode.com/problems/find-if-digit-game-can-be-won
# Completed 2026/04/21
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for n in nums:
            if len(str(n)) == 1:
                single += n
            else:
                double += n
        if abs(single - double) > 0:
            return True
        else:
            return False