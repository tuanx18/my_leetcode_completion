# [EASY] https://leetcode.com/problems/n-repeated-element-in-size-2n-array
# Completed 2026/05/04
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        prs = []
        for k, v in freq.items():
            prs.append((k, v))
        prs.sort(key=lambda x: x[1], reverse=True)
        return prs[0][0]