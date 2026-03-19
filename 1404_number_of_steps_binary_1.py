# [MEDIUM] https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# Completed 2026/02/26

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        step = 0
        n = int(s, 2)
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n += 1
            step += 1
        return step