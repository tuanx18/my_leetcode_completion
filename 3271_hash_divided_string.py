# [MEDIUM] https://leetcode.com/problems/hash-divided-string
# Completed 2026/03/30
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        mapping = {}
        rev_map = {}
        for i in range(26):
            char = chr(ord('a') + i)
            mapping[char] = i
            rev_map[i] = char
        
        res = ''
        for i in range(0, len(s), k):
            point = 0
            for j in range(i, i + k):
                point += mapping[s[j]]
            res += rev_map[point % 26]
        return res