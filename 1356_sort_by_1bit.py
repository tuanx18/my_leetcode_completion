# [EASY] https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits
# Completed 2026/02/25
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(arr)):
            n = 0
            for b in bin(arr[i]):
                if b == '1':
                    n += 1000000
                n += arr[i]
            dct[i] = n
        res = [k for k, v in sorted(dct.items(), key = lambda x:x[1])]
        res_bin = [arr[l] for l in res]
        return res_bin