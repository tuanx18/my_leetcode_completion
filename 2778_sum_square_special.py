# [EASY] https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Completed 2026/04/20
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i, v in enumerate(nums):
            if n % (i + 1) == 0:
                res += (v ** 2)
        
        return res