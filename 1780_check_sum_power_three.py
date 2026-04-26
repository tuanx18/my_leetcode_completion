# [MEDIUM] https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
# Completed 2026/04/21
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
