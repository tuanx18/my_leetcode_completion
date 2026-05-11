# [EASY] https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
# Completed 2026/05/04
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        i = 1
        while i < len(nums): 
            if nums[i] <= nums[i-1]:
                to_add = nums[i-1] - nums[i] + 1
                nums[i] += to_add
                res += to_add 
            i += 1
        return res