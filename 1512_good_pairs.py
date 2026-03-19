# [EASY https://leetcode.com/problems/number-of-good-pairs/
# Completed 2026/03/13
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {} 
        total = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for k, v in freq.items():
            total += v * (v - 1) / 2
        return int(total)