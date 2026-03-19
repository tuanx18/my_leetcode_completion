# [EASY] https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three
# Completed 2026/03/17
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if i % 3 != 0:
                ans += 1
        return ans