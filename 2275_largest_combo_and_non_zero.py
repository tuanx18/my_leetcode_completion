# [MEDIUM] https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
# Completed 2026/04/19
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bnr = []
        max_len = len(bin(max(candidates))) - 2
        for i in candidates:
            b = bin(i)[2:]
            b = [ch for ch in b[::-1]]
            while len(b) < max_len:
                b.append('0')
            bnr.append(b)
        
        trans_bnr = list(zip(*bnr))
        trans_bnr = [list(z) for z in trans_bnr]

        res = 0
        for combo in trans_bnr:
            res = max(res, combo.count("1"))
        
        return res