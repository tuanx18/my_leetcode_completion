# [MEIDIM] https://leetcode.com/problems/watering-plants
# Completed 2026/04/15
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        res = 0
        for i in range(len(plants)):
            if cap >= plants[i]:
                cap -= plants[i]
                res += 1
            else:
                res += (i + 1 + i)
                cap = capacity - plants[i]
        return res
                
