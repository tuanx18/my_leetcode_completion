# [EASY] https://leetcode.com/problems/number-of-arithmetic-triplets/
# Completed 2026/03/17
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        seen = set(nums)
        res = 0
        for i in nums:
            if i + diff in seen and i + diff + diff in seen:
                res += 1
        return res