# [EASY] https://leetcode.com/problems/decode-xored-array
# Completed 2026/03/17
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(res[-1] ^ i)
        return res