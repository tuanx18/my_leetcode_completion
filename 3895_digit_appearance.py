# [MEDIUM] https://leetcode.com/problems/count-digit-appearances
# Completed 2026/05/04
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = 0
        for n in nums:
            res += str(n).count(str(digit))
        return res