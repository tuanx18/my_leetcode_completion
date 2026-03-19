# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation
# 2026/02/21

class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def prime(n):
            if n == 1:
                return False
            path = []
            for num in range(2, n + 1):
                if n % num == 0:
                    path.append(num)
            if len(path) == 1:
                return True
            else: 
                return False

        res = 0
        seen = set()

        for i in range(left, right + 1):
            bits = 0
            n = i
            while n > 0:
                if n & 1 == 1:
                    bits += 1
                n >>= 1 

            if bits in seen:
                res += 1
                continue
            else:
                if prime(bits):
                    seen.add(bits)
                    res += 1
                else:
                    continue
        return res