# [EASY] https://leetcode.com/problems/find-center-of-star-graph
# Completed 2026/03/16
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n1 = set(edges[0])
        n2 = set(edges[1])
        ans = n1.intersection(n2)
        return next(iter(ans))