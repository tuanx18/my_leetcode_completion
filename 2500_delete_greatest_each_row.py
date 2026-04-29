# [EASY] https://leetcode.com/problems/delete-greatest-value-in-each-row/
# Completed 2026/04/28
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        for r in grid:
            r.sort(reverse=True)

        trn = list(zip(*grid))
        trn = [list(x) for x in trn]

        res = 0
        for r in trn:
            res += max(r)
        
        return res