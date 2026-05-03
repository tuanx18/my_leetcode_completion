# [EASY] https://leetcode.com/problems/remove-trailing-zeros-from-a-string
# Completed 2026/05/03
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.strip("0")