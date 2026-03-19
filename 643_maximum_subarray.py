# [EASY] https://leetcode.com/problems/maximum-average-subarray-i
# Completed 2026/03/01
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if k > len(nums):
            return 0
        l = 0
        r = k
        total = sum(nums[l:r])
        ans = total / k
        l += 1
        r += 1

        while r <= len(nums):
            print(l, r)
            total = total - nums[l - 1] + nums[r - 1]
            ans = max(total / k, ans)
            l += 1
            r += 1
        return ans