# [EASY] https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
# Completed 2026/03/29
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= k:
                return i