# [EASY] https://leetcode.com/problems/mirror-distance-of-an-integer
# Completed 2026/04/18
class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        s = [ch for ch in s]
        s.reverse()
        s = ''.join(s)
        return abs(int(s) - n)