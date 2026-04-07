# [EASY] https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Completed 2026/04/07
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        matrix_p = list(zip(*matrix))
        matrix_p = [list(z) for z in matrix_p]
        
        min_row = set()
        max_col = set()

        for r in matrix:
            min_row.add(min(r))
        
        for c in matrix_p:
            max_col.add(max(c))
        
        share = min_row.intersection(max_col)
        return list(share)