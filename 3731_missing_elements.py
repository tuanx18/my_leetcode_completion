# [EASY] https://leetcode.com/problems/find-missing-elements/
# Completed 2026/03/31
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        uniq = set(nums)
        mn = min(nums)
        mx = max(nums)
        res = []
        for i in range(mn, mx + 1):
            if i not in uniq:
                res.append(i)
        return res