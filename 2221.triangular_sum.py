# [MEDIUM] https://leetcode.com/problems/find-triangular-sum-of-an-array/
# Completed 2026/04/03
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        rem = nums[:]
        while n > 1:
            curr = []
            for i in range(len(rem) - 1):
                curr.append(rem[i] + rem[i+1])
            rem = curr[:]
            n = len(rem)
        return rem[0] % 10