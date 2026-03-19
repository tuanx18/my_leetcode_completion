# [EASY] https://leetcode.com/problems/find-the-highest-altitude
# Completed 2026/03/01

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr = 0
        ans = 0
        for i in range(len(gain)):
            curr += gain[i]
            ans = max(ans, curr)
        return ans
        