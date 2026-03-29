# [EASY] https://leetcode.com/problems/count-symmetric-integers
# Completed 2026/03/24
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if len(str(i)) % 2 == 0:
                s = [ch for ch in str(i)]
                # mid = len(s) // 2
                left = s[:(len(s) // 2)]
                right = s[(len(s) // 2):]
                left = [int(x) for x in left]
                right = [int(y) for y in right]
                if sum(left) == sum(right):
                    res += 1
        return res