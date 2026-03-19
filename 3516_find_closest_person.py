# [EASY] https://leetcode.com/problems/find-closest-person
# Completed 2026/02/22
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        p1 = abs(z - x)
        p2 = abs(z - y)
        if p1 == p2:
            return 0
        if p1 < p2:
            return 1
        else:
            return 2