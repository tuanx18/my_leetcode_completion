# [MEDIUM] https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram
# Completed 2026/03/29
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqa = {}
        freqb = {}
        for i in range(len(s)):
            freqa[s[i]] = freqa.get(s[i], 0) + 1
            freqb[t[i]] = freqb.get(t[i], 0) + 1
        target = {}
        for k, v in freqb.items():
            target[k] = v - freqa.get(k, 0)
        res = 0
        for val in target.values():
            if val > 0:
                res += val
        return res