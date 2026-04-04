# [EASY] https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
# Completed 2026/04/04
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while len(word) < k:
            new = ''
            for ch in word:
                new_ch = chr(ord(ch) + 1)
                new += new_ch
            word += new
        return word[k-1]