# [EASY] https://leetcode.com/problems/number-of-laser-beams-in-a-bank
# Completed 2026/03/17
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 9996
        for row in bank:
            gun = 0
            for ch in row:
                if ch == '1':
                    gun += 1
            if prev != 9996:
                if gun == 0:
                    pass
                else:
                    res += prev * gun
                    prev = gun
            elif prev == 9996:
                prev = gun
        return res
                
