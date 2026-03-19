# https://leetcode.com/problems/reverse-prefix-of-word/
# Completed 2026/02/24
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        
        new = []
        for c in range(len(word)):
            if word[c] != ch:
                new.append(word[c])
            elif word[c] == ch:
                new.append(word[c])
                new.reverse()
                return ''.join(new) + word[c+1:]

        