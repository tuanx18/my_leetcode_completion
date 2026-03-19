# [EASY] https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Completed 2026/03/15
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for o in operations:
            if "-" in o:
                res -= 1 
            else:
                res += 1
        return res