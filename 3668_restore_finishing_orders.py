# [EASY] https://leetcode.com/problems/restore-finishing-order/
# Completed 2026/03/13
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        fr = set(friends)
        res = []
        for i in order:
            if i in fr:
                res.append(i)
        return res