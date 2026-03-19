# [MEDIUM] https://leetcode.com/problems/find-kth-bit-in-nth-binary-string
# Completed 2026/03/03
class Solution:
    @staticmethod
    def findKthBit(n: int, k: int) -> str:
        def rev_invert(s):
            inv = ['1' if ch == '0' else '0' for ch in s]
            inv.reverse()
            return ''.join(inv)
        
        curr = '0'
        for i in range(n - 1):
            curr = curr + '1' + rev_invert(curr)
        print(curr)
        return curr[k - 1]

n = 4
k = 11
sol = Solution.findKthBit(n,k)