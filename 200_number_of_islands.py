# [MEDIUM] https://leetcode.com/problems/number-of-islands/
# Completed 2026/04/29
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(a, b):
            nonlocal res
            if grid[a][b] == "0":
                return
            else:   
                grid[a][b] = "0"

                if a < rows-1:
                    dfs(a+1,b)
                if b < cols-1:
                    dfs(a,b+1)
                if a > 0:
                    dfs(a-1,b)
                if b > 0:
                    dfs(a,b-1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
