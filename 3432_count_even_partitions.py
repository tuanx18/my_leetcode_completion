# [EASY] https://leetcode.com/problems/count-partitions-with-even-sum-difference
# Completed 2026/03/17
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # res = 0
        # i = 0
        # left = 0
        # right = -sum(nums)
        # while i < len(nums):
        #     left += nums[i]
        #     right -= nums[i]
        s = sum(nums)
        if s % 2 == 0:
            return len(nums) - 1
        else:
            return 0