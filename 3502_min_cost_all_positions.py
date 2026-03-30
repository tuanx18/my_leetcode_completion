# [EASY] https://leetcode.com/problems/minimum-cost-to-reach-every-position/
# Completed 2026/03/30
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = []
        curr = float('inf')
        for i in cost:
            curr = min(curr, i)
            res.append(curr)
        return res