# [EASY] https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Completed 2026/03/17
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        pro = 1
        sm = 0
        for i in s:
            pro *= int(i)
            sm += int(i)
        return pro - sm