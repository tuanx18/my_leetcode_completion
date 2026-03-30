# [EASY] https://leetcode.com/problems/harshad-number/
# Completed 2026/03/30
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        sum_dig = 0
        for ch in s:
            sum_dig += int(ch)
        if x % sum_dig == 0:
            return sum_dig
        else:
            return -1