# [EASY] https://leetcode.com/problems/find-the-integer-added-to-array-i
# Completed 2026/03/24
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)