# [MEDIUM] https://leetcode.com/problems/letter-tile-possibilities
# Completed 2026/04/09
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        res = 0
        def backtrack():
            nonlocal res
            for i in range(len(tiles)):
                if used[i]:
                    continue
                if not used[i-1] and tiles[i] == tiles[i-1] and i > 0:
                    continue
                
                used[i] = True
                res += 1
                backtrack()
                used[i] = False
        backtrack()
        return res 