# [MEDIUM] https://leetcode.com/problems/greatest-common-divisor-of-strings
# Completed 2026/02/22

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        m = len(str1)
        n = len(str2)

        if str1 + str2 == str2 + str1 and m % n == 0:
            return str2
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def divi(x):
            res = []
            for _ in range(x, 0, -1):
                if x % _ == 0:
                    res.append(_)
            return res
        
        def sliding_window(nums, k):
            return [nums[j:j + k] for j in range(len(nums) + 1 - k)]

        longest = divi(gcd(m, n))
        seen = set()

        for i in longest:   # i = 2
            sub = sliding_window(str2, i)
            for subset in sub:
                if subset not in seen:
                    seen.add(subset)
                    if str1 + subset == subset + str1 and str2 + subset == subset + str2:
                        return subset
        return ''