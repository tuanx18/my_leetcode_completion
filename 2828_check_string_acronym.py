# [EASY] https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words
# Completed 2026/05/03
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr = ''
        for l in words:
            acr += l[0]
        
        if acr == s:
            return True
        return False