# [EASY] https://leetcode.com/problems/compute-alternating-sum
# Completed 2026/03/13
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                ans += nums[i]
            else:
                ans -= nums[i]
        return ans