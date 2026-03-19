# [EASY] https://leetcode.com/problems/find-resultant-array-after-removing-anagrams
# Completed 2026/03/13
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) <= 1:
            return words
        checking = '6969'
        res = []
        i = 0
        while i < len(words):
            curr = ''.join(sorted(words[i]))
            if curr == checking:
                i += 1
            elif curr != checking:
                checking = curr
                res.append(words[i])
        return res