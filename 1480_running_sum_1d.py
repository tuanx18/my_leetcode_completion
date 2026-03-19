# [EASY] https://leetcode.com/problems/running-sum-of-1d-array/
# Completed 2026/03/17
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pref = 0
        res = []
        for i in nums:
            pref += i
            res.append(pref)
        return res