# [EASY] https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/
# Completed 2026/04/25
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        start = False
        for i in nums:
            if not start and i % 2 == 0:
                start = True
                res = i
            elif i % 2 == 0:
                res |= i
        return res