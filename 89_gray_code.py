# [MEDIUM] https://leetcode.com/problems/gray-code/
# Completed 2026/04/17
class Solution:
    def grayCode(self, n: int) -> List[int]:
        curr = '0' * n
        res = [0]
        for bit in range(n):
            for num in reversed(res):
                res.append(num + (1 << bit))
        return res
