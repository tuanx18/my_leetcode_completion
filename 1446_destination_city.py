# [EASY] https://leetcode.com/problems/destination-city
# Completed 2026/04/18
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        road = {}
        for b, e in paths:
            road[b] = e

        head = set(road.keys())
        tail = set(road.values())

        f = tail - head
        res = next(iter(f))

        return res