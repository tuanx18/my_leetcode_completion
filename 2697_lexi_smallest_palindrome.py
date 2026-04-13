# [EASY] https://leetcode.com/problems/lexicographically-smallest-palindrome/
# Completed 2026/04/13
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        mid = len(s) // 2
        
        l = 0
        r = len(s) - 1

        lres = ''
        rres = ''

        while l <= r:
            if l == r:
                lres += s[l]
            elif ord(s[l]) <= ord(s[r]):
                lres += s[l]
                rres = s[l] + rres
            else:
                lres += s[r]
                rres = s[r] + rres
            l += 1
            r -= 1
        return lres + rres
