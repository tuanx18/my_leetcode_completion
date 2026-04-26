# [EASY] https://leetcode.com/problems/traffic-signal-color/
# Completed 2026/04/26
class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid"