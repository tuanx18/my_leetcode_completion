# [EASY] https://leetcode.com/problems/minimum-number-game/
# Completed 2026/03/23
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        res = []
        nums.sort()

        i = 0
        while i < len(nums):
            res.append(nums[i+1])
            res.append(nums[i])
            i += 2
        return res