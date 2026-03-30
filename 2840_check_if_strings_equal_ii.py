# [MEDIUM] https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii
# Completed 2026/03/30
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = {}
        even2 = {}
        odd1 = {}
        odd2 = {}
        i = 0
        while i < len(s1):
            if i % 2 == 0:
                even1[s1[i]] = even1.get(s1[i], 0) + 1
                even2[s2[i]] = even2.get(s2[i], 0) + 1
            else:
                odd1[s1[i]] = odd1.get(s1[i], 0) + 1
                odd2[s2[i]] = odd2.get(s2[i], 0) + 1
            i += 1
        for k, v in even1.items():
            if v != even2.get(k, 0):
                return False
        for k, v in odd1.items():
            if v != odd2.get(k, 0):
                return False
        return True