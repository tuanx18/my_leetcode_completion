# [EASY] https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
# Completed 2026/04/19
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        x = 0
        val = max(nums)
        res = 0
        while x < k:
            res += val
            val += 1
            x += 1
        return res