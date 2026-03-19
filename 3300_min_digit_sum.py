# [EASY] https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Completed 2026/03/17
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 800000
        for i in nums:
            curr = 0
            for di in str(i):
                curr += int(di)
            ans = min(ans, curr)
        return ans