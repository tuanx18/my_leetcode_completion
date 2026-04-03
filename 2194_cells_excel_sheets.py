# [EASY] https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
# Completed 2026/04/03
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = s.split(':')
        span = ord(cells[1][0]) - ord(cells[0][0])
        first = int(cells[0][1])
        last = int(cells[1][1])
        res = []
        for i in range(span + 1):
            for j in range(first, last + 1):
                char = chr(ord(cells[0][0]) + i)
                res.append(char + str(j))
        return res