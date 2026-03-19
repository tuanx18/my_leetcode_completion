# [EASY] https://leetcode.com/problems/transform-array-by-parity
# Completed 2026/03/15
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        zi = 0
        oi = 0
        for i in nums:
            if i % 2 == 0:
                zi += 1
            else:
                oi += 1
        return [0] * zi + [1] * oi