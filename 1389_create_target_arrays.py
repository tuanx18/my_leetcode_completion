# [EASY] https://leetcode.com/problems/create-target-array-in-the-given-order
# Completed 2026/03/18
class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res