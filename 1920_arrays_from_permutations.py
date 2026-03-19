# [EASY] https://leetcode.com/problems/build-array-from-permutation/
# Completed 2026/03/13
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(nums[i])
        return res