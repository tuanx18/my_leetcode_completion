# [EASY] https://leetcode.com/problems/flood-fill
# Completed 2026/04/29
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if image[r][c] != ori:
                return

            if image[r][c] == ori:
                image[r][c] = color
            
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        ori = image[sr][sc]
        if color == ori:
            return image

        dfs(sr, sc)
        return image