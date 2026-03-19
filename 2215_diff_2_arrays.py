# [EASY] https://leetcode.com/problems/find-the-difference-of-two-arrays
# Completed 2026/02/28
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1 = set(nums1)
        s2 = set(nums2)

        res1 = s1 - s2
        res2 = s2 - s1
        
        res = [list(res1), list(res2)]
        return res