# [EASY] https://leetcode.com/problems/is-subsequence
# Completed 2026/02/24
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t: 
            return False
        n = 0
        target = len(s)
        for i in range(len(t)):
            if t[i] == s[n]:
                n += 1
            
            if n == target:
                return True
        return False