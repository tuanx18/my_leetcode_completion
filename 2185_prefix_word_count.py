# [EASY] https://leetcode.com/problems/counting-words-with-a-given-prefix
# Completed 2026/04/10
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        res = 0
        for w in words:
            if w[0:n] == pref:
                res += 1
        return res