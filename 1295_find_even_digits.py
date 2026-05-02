# [EASY] https://leetcode.com/problems/find-numbers-with-even-number-of-digits
# Completed 2026/05/02
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        return res