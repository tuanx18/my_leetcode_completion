# [EASY] https://leetcode.com/problems/sum-of-unique-elements/
# Completed 2026/04/28
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        for i, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
        
        res = 0
        for k, v in freq.items():
            if v == 1:
                res += k
        return res