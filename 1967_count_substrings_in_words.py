# [EASY] https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Completed 2026/03/29
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for s in patterns:
            if s in word:
                res += 1
        return res