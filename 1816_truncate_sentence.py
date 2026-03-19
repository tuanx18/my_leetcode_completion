# [EASY] https://leetcode.com/problems/truncate-sentence
# Completed 2026/03/16
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        w = s.split(' ')
        return ' '.join(w[:k])