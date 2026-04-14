# [MEDIUM] https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# Completed 2026/04/14
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for i in range(num1, num2 + 1):
            s = str(i)
            l = len(s)
            if l < 3:
                continue

            s = [ch for ch in s]

            for idx in range(1, l - 1):
                if s[idx] < s[idx - 1] and s[idx] < s[idx + 1]:
                    res += 1
                elif s[idx] > s[idx - 1] and s[idx] > s[idx + 1]:
                    res += 1
        return res

