# [MEDIUM] https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box
# Completed 2026/02/22

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(boxes)):
            path = 0
            for j in range(len(boxes)):
                if i != j:
                    if boxes[j] == '1':
                        path += abs(i - j)
            res.append(path)
        return res