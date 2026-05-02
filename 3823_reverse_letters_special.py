# [EASY] https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string 
# Completed 2026/04/30
class Solution:
    def reverseByType(self, s: str) -> str:
        cha = []
        spe = []

        letters = set()
        for i in range(26):
            c = chr(ord('a') + i)
            letters.add(c)

        for ch in s:
            if ch in letters:
                cha.append(ch)
            else:
                spe.append(ch)
        
        cha.reverse()
        spe.reverse()

        a = 0
        b = 0
        res = ''

        for n in range(len(s)):
            if s[n] in letters:
                res += cha[a]
                a += 1
            else:
                res += spe[b]
                b += 1
        return res
