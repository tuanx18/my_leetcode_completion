# [EASY] https://leetcode.com/problems/separate-the-digits-in-an-array/
# Completed 2026/03/20
class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            s = str(i)
            for ch in s:
                res.append(int(ch))
        return res