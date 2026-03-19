# [EASY] https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# Completed 2026/03/16
class Solution:
    @staticmethod
    def minBitFlips(start: int, goal: int) -> int:
        b1 = bin(start)[-1:1:-1]
        b2 = bin(goal)[-1:1:-1]
        if len(b1) > len(b2):
            b2 += (len(b1) - len(b2)) * '0' 
        elif len(b2) > len(b1):
            b1 += (len(b2) - len(b1)) * '0' 
        ans = 0
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                ans += 1
        return ans

start = 7
goal = 10
sol = Solution.minBitFlips(start, goal)
print(sol)