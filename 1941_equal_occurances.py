# [EASY] https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences
# Completed 2026/05/05
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
        uniq = set(freq.values())
        if len(uniq) == 1:
            return True
        return False