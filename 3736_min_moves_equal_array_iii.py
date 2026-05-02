# [EASY] https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii
# Completed 2026/04/30
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        res = 0
        for i in nums:
            res += target - i
        return res