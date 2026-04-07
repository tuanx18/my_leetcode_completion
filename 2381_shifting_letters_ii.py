# [MEDIUM] https://leetcode.com/problems/shifting-letters-ii
# Completed 2026/04/06
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        
        # Step 1 — Difference array
        diff = [0] * (n + 1)

        for l, r, d in shifts:
            val = 1 if d == 1 else -1
            diff[l] += val
            diff[r + 1] -= val

        # Step 2 — Prefix sum to build shift values
        curr = 0
        res = []

        for i in range(n):
            curr += diff[i]

            # Convert character
            new_char = chr(
                (ord(s[i]) - ord('a') + curr) % 26
                + ord('a')
            )
            res.append(new_char)

        return ''.join(res)