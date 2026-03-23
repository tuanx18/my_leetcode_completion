# [EASY]
# Completed 2026/03/23
class Solution:
    @staticmethod
    def largestLocal(grid: list[list[int]]) -> list[list[int]]:

        n = len(grid) - 2
        mat = [[0]*n for _ in range(n + 2)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = max(grid[i][j], grid[i][j + 1], grid[i][j + 2])
        print(mat)

        res = [[0]*n for _ in range(n)]
        for i in range(len(res)):
            for j in range(len(res)):
                res[i][j] = max(mat[i][j], mat[i+1][j], mat[i+2][j])
        return res

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
sol = Solution.largestLocal(grid)
print(sol)