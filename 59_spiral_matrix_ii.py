# [MEDIUM]
# Completed 2026/03/22
class Solution:
    @staticmethod
    def generateMatrix(n: int) -> list[list[int]]:
        curr = 1
        r = c = min_r = min_c = 0
        max_r = n - 1
        max_c = n - 1
        mat = [[0]*n for _ in range(n)]

        while curr <= n ** 2:
            mat[r][c] = curr
            print("row: ", r, "col: ", c)

            if r == min_r and c < max_c:
                c += 1
                if c == max_c:
                    min_r += 1

            elif c == max_c and r < max_r:
                r += 1
                if r == max_r:
                    max_c -= 1

            elif r == max_r and c > min_c:
                c -= 1
                if c == min_c:
                    max_r -= 1

            elif c == min_c and r > min_r:
                r -= 1
                if r == min_r:
                    min_c += 1
            curr += 1
        return mat

n = 3
sol = Solution.generateMatrix(n)
print(sol)