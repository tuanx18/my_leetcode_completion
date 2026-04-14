# [EASY] https://leetcode.com/problems/self-dividing-numbers
# Completed 2026/04/14
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            n = str(i)
            s = set(str(s) for s in n)
            if len(s) == 1:
                res.append(i)
                continue
            new = True
            for ch in s:
                if ch == '0':
                    new = False
                    break
                if i % int(ch) != 0:
                    new = False
                    break
            if new:
                res.append(i)
        return res