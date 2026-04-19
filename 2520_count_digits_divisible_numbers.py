# [EASY] https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Completed 2026/04/18
class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        s = str(num)
        for ch in s:
            if num % int(ch) == 0:
                res += 1
        return res