# [EASY] https://leetcode.com/problems/defuse-the-bomb
# Completed 2026/05/06
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        
        res = [0] * len(code)
        L = len(code)

        for i in range(L):
            if k > 0:
                for x in range(1, k + 1):
                    res[i] += code[(i + x) % L]
            else:
                kn = abs(k)
                for x in range(1, kn + 1):
                    res[i] += code[(i - x) % L]

        return res
