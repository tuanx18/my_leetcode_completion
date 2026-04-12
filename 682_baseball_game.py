# [EASY] https://leetcode.com/problems/baseball-game/
# Completed 2026/04/12
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for n in operations:
            if n == 'C':
                score.pop()
            elif n == 'D':
                score.append(score[-1] * 2)
            elif n == "+":
                score.append(score[-2] + score[-1])
            else:
                score.append(int(n))
        # print(score)
        return sum(score)