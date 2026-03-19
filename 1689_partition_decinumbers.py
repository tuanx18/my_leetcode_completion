# [MEDIUM] https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers
# Completed 2026/03/01

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        ans = 0
        for i in n:
            ans = max(ans, int(i))
        return ans