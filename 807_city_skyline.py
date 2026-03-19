# [MEDIUM][Graph] https://leetcode.com/problems/max-increase-to-keep-city-skyline
# Completed 2026/03/17
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        row_max = []
        for r in grid:
            row_max.append(max(r))
        col_max = []
        for ri in range(len(grid)):
            mcol = 0
            for ci in range(len(grid[0])):
                mcol = max(mcol, grid[ci][ri])
            col_max.append(mcol)
        print(row_max, col_max)

        for _row in range(len(grid)):
            for _col in range(len(grid[0])):
                new_height = min(row_max[_row], col_max[_col])
                if grid[_row][_col] < new_height:
                    ans += new_height - grid[_row][_col] 
        return ans