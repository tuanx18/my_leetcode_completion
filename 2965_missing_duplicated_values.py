# [EASY] https://leetcode.com/problems/find-missing-and-repeated-values
# Completed 2026/04/09
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        missing = None
        mx = len(grid)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] not in seen:
                    seen.add(grid[r][c])
                else:
                    missing = grid[r][c]
        for i in range(1, (mx ** 2) + 1):
            if i not in seen:
                dup = i
        return [missing, dup]
        

