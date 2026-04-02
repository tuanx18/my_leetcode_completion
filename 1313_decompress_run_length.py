# [EASY] https://leetcode.com/problems/decompress-run-length-encoded-list
# Completed 2026/04/02
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            new = [nums[i+1]] * nums[i]
            res.extend(new)
        return res