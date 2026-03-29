# [EASY] https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Completed 2026/03/29
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            words = s.split()
            ans = max(ans, len(words))
        return ans