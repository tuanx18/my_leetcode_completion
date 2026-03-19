# [EASY] https://leetcode.com/problems/n-th-tribonacci-number
# Completed 2026/03/02
class Solution:
    @staticmethod
    def tribonacci(n: int) -> int:

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        nums = [0, 1, 1]  # T0, T1, T2
        for i in range(3, n + 1):  # build up to Tn (inclusive)
            nums.append(nums[-1] + nums[-2] + nums[-3])
        return nums[n]

n = 4
sol = Solution.tribonacci(n)
print(sol)
            