# [MEDIUM] https://leetcode.com/problems/sort-the-matrix-diagonally
# Completed 2026/05/03 
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        def sort_dia(a, b):
            sa, sb = a, b

            vals = []
            while a <= (rows - 1) and b <= (cols - 1):
                vals.append(mat[a][b])
                a += 1
                b += 1
            print(vals)
            
            if len(vals) > 1:
                vals.sort(reverse=True)
                while sa <= (rows - 1) and sb <= (cols - 1):
                    mat[sa][sb] = vals.pop()
                    sa += 1
                    sb += 1
        
        r = rows - 1
        c = 0

        while c <= cols - 1:
            if c == 0 and r != 0:
                sort_dia(r, c)
                r -= 1
            elif r == 0:
                sort_dia(r, c)
                c += 1
        return mat


