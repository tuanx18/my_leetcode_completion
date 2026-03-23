# [EASY] https://leetcode.com/problems/xor-operation-in-an-array/
# Completed 2026/03/23
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        turn = 1
        res = start
        while turn < n:
            res ^= start + 2
            start += 2
            turn += 1
        return res