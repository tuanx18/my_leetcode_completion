# [EASY] https://leetcode.com/problems/move-zeroes
# Completed 2026/02/22
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last], nums[i] = nums[i], nums[last]
                last += 1