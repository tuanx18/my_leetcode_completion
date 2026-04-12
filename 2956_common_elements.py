# [EASY] https://leetcode.com/problems/find-common-elements-between-two-arrays/
# Completed 2026/04/10
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = 0
        a2 = 0
        sn1 = set(nums1)
        sn2 = set(nums2)
        for i in nums1:
            if i in sn2:
                a1 += 1
        for i in nums2:
            if i in sn1:
                a2 += 1
        return [a1, a2]