# [EASY] https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
# Completed 2026/03/22
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for i in range(3):
            mat = list(zip(*mat[::-1]))
            mat = [list(row) for row in mat]

            if mat == target:
                return True
        return False