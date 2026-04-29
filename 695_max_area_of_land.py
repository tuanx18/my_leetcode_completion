# [MEDIUM] https://leetcode.com/problems/max-area-of-island/
# Completed 2026/04/29
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(a, b):
            if a < 0 or b < 0 or a >= rows or b >= cols:  
                return 0
            if grid[a][b] == 0:
                return 0
            
            grid[a][b] = 0
            return 1 + dfs(a+1,b) + dfs(a,b+1) + dfs(a-1,b) + dfs(a,b-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res