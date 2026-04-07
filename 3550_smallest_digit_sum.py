# [EASY] https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index
# Completed 2026/04/07
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            curr = 0
            for n in str(v):
                curr += int(n)
            
            if i == curr:
                return i
        return -1