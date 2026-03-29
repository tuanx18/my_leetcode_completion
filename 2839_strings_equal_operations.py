# [EASY] https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i
# Completed 2026/03/29
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        i = 2
        while i < len(s1):
            if s1[i] == s2[i-2] and s2[i] == s1[i-2]:
                i += 1
                continue
            if s1[i] == s2[i] and s1[i-2] == s2[i-2]:
                i += 1
                continue
            return False
        return True
            

