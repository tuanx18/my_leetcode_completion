# [EASY] https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Completed 2026/03/15
class Solution:
    @staticmethod
    def minCostClimbingStairs(cost):
        prev2, prev1 = 0, 0
        for c in cost:
            print("prev2: ", prev2, " prev1: ", prev1)
            prev2, prev1 = prev1, c + min(prev1, prev2)
        return min(prev1, prev2)

cost = [1,100,1,1,1,100,1,1,100,1]
sol = Solution.minCostClimbingStairs(cost)
print(sol)