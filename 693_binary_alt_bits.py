class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = None
        while n > 0:
            bit = n & 1
            if bit == prev:
                return False
            prev = bit
            n >>= 1
        return True
            