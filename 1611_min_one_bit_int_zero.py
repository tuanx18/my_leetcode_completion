# [HARD] https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero
# Completed 2026/04/16
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        bnr = bin(n)[2:]
        bnr = [i for i in bnr[::-1]]
        
        pwr = 0
        curr = 0
        tot = 0

        for b in bnr:
            tot += (1 << pwr)
            pwr += 1
            if b == '1':
                curr = tot- curr
        return curr