# [MEDIUM] 
# Completed 2026/03/23
class Solution:
    @staticmethod
    def spiralOrder(matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
        r = c = min_r = min_c = 0
        max_r = len(matrix) - 1
        max_c = len(matrix[0]) - 1
        total = len(matrix) * len(matrix[0])

        while len(res) < total:
            while c <= max_c and len(res) < total:
                res.append(matrix[r][c])
                c += 1
            c -= 1
            r += 1
            min_r += 1

            while r <= max_r and len(res) < total:
                res.append(matrix[r][c])
                r += 1
            r -= 1
            c -= 1
            max_c -= 1

            while c >= min_c and len(res) < total:
                res.append(matrix[r][c])
                c -= 1
            c += 1
            r -= 1
            max_r += 1

            while r >= min_r and len(res) < total:
                res.append(matrix[r][c])
                r -= 1
            r += 1
            c += 1
            min_c -= 1
        return res 

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
sol = Solution.spiralOrder(matrix)
print(sol)