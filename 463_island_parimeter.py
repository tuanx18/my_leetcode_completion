# [EASY] https://leetcode.com/problems/island-perimeter
# Completed 2026/04/29
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        par = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    par += 4
                
                    if r > 0 and grid[r-1][c] == 1:
                        par -= 2
                    
                    if c > 0 and grid[r][c-1] == 1:
                        par -= 2
        return par