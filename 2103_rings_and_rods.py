# [EASY] https://leetcode.com/problems/rings-and-rods
# Completed 2026/04/21
class Solution:
    def countPoints(self, rings: str) -> int:
        hold = [set() for _ in range(3)]
        for i in range(0, len(rings), 2):
            if rings[i] == "B":
                hold[0].add(int(rings[i+1]))
            elif rings[i] == "G":
                hold[1].add(int(rings[i+1]))
            elif rings[i] == "R":
                hold[2].add(int(rings[i+1]))
        
        mutual = hold[0].intersection(hold[1]).intersection(hold[2])
        return len(mutual)