# [MEDIUM] https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# Completed 2026/03/17
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        step = 0
        ans = 0
        x = len(piles) - 2
        while step < len(piles):
            ans += piles[x]
            x -= 2
            step += 3
        return ans

piles = [2,4,1,2,7,8] 
# output = 9 (1, 2, 4) - (2, 7, 8)
