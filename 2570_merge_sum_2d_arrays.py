# [EASY] https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# Completed 2026/04/30
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        freq = {}
        for i, v in nums1:
            freq[i] = v
        
        for i, v in nums2:
            freq[i] = freq.get(i, 0) + v
        
        res = []
        for i, v in freq.items():
            res.append([i, v])
        
        res.sort(key=lambda x:x[0])
        return res