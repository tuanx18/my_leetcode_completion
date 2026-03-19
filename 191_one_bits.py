class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_bit = 0
        while n > 0:
            one_bit += n & 1
            n >>= 1
        return one_bit
        