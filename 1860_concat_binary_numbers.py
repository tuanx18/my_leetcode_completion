# [MEDIUM] https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers
# Completed 2026/02/28

class Solution(object):
    @staticmethod
    def concatenatedBinary(n):
        """
        :type n: int
        :rtype: int
        """
        csum = 0
        modu = 10 ** 9 + 7

        for i in range(1, n + 1):
            bn = len(bin(i)) - 2
            csum = (csum << bn) + i

        return csum % modu

        # i = 1 -> b = 1 -> sum = 1
        # i = 2 -> b = 10 -> sum = old_sum * (2 ^ bit count) + i = 1 * 2^2 + 2 = 6
        # i = 3 -> b = 11 -> sum = old_sum * (2 ^ bit count) + i = 6 * 2^2 + 3 = 27


# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.
n = 3
sol = Solution.concatenatedBinary(n)
print(sol)