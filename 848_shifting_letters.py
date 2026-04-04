# [MEDIUM] https://leetcode.com/problems/shifting-letters/
# Completed 2026/04/04
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alpha = {}
        ralpha = {}
        for l in range(26):
            alpha[chr(ord('a') + l)] = l
            ralpha[l] = chr(ord('a') + l)

        tot = sum(shifts)
        prefix = [tot % 26]
        for i in shifts[::]:
            tot -= i
            prefix.append(tot % 26)
        prefix.pop()
        # print(prefix)

        def shift(char, unit) -> str:
            idx = (alpha[char] + unit) % 26
            return ralpha[idx]

        ss = [ch for ch in s]
        for i in range(len(ss)):
            print(ss[i], prefix[i])
            ss[i] = shift(ss[i], prefix[i])
        return ''.join(ss)
