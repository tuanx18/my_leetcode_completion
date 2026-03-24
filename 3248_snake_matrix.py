# https://leetcode.com/problems/snake-in-matrix/
# Completed 2026/03/24
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        m = l = 0
        for com in commands:
            if com == "LEFT":
                l -= 1
            elif com == "RIGHT":
                l += 1
            elif com == "UP":
                m -= 1
            else:
                m += 1
        
            num = 0
            mat = []

        for i in range(n):
            row = []
            for j in range(n):
                row.append(num)
                num += 1
            mat.append(row)
        
        # print(m,l, mat)
        return mat[m][l]


n = 3
commands = ["RIGHT","DOWN"]
sol = Solution.finalPositionOfSnake(n, commands)
print(sol)