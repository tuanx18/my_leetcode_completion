# [EASY] https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
# Completed 2026/04/16
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        disc = []
        for i in range(len(prices)):
            j = i + 1
            curr = prices[i]
            while j < len(prices):
                if prices[j] <= prices[i]:
                    curr -= prices[j]
                    break
                j += 1
            disc.append(curr)
        return disc