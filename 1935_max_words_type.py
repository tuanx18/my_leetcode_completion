# [EASY] https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# Completed 2026/04/05
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0
        for w in words:
            valid = True
            for ch in brokenLetters:
                if ch in w:
                    valid = False
                    break
                      
            if valid:
                res += 1
                
        return res