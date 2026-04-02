# [EASY] https://leetcode.com/problems/find-maximum-number-of-string-pairs
# Completed 2026/04/02
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        rev = []
        for ch in words:
            rev.append(ch[::-1])
        
        res = 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == rev[j]:
                    res += 1
                    break
        return res