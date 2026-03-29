# [MEDIUM] https://leetcode.com/problems/reveal-cards-in-increasing-order
# Completed 2026/03/29
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        stack = []
        while deck:
            card = deck.pop()
            if not stack:
                stack.append(card)
            elif len(stack) == 1:
                stack.insert(0, card)
            elif len(stack) >= 2:
                stack = [stack[-1]] + stack[:len(stack) - 1]
                stack.insert(0, card)
        return stack
