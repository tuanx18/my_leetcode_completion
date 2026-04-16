# [EASY] https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Completed 2026/04/16
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        res = 0
        for j in nums:
            target = j + k
            res += freq.get(target, 0)
        
        return res