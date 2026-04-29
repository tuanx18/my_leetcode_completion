# [MEDIUM] https://leetcode.com/problems/surrounded-regions/
# Completed 2026/04/29
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        sb = [["NA"] * cols for _ in range(rows)]

        def dfs_safe(a, b):
            if a < 0 or b < 0 or a >= rows or b >= cols:
                return
            if sb[a][b] == "S":
                return
            
            if board[a][b] != "O":
                return
            sb[a][b] = "S"

            dfs_safe(a+1,b)
            dfs_safe(a-1,b)
            dfs_safe(a,b+1)
            dfs_safe(a,b-1)
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == "O":
                        dfs_safe(r, c)
        
        def dfs(a, b):
            if a < 0 or b < 0 or a >= rows or b >= cols:
                return
            if board[a][b] == "X":
                return
            
            board[a][b] = "X"
            dfs(a+1,b)
            dfs(a-1,b)
            dfs(a,b+1)
            dfs(a,b-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and sb[r][c] != "S":
                    dfs(r, c)
