# [MEDIUM] https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
# Completed 2026/03/14
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        prev = 0
        for p in pref:
            res.append(prev ^ p)
            prev = p
        return res