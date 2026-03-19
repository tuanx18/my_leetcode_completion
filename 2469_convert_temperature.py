# [EASY] https://leetcode.com/problems/defanging-an-ip-address/
# Completed 2026/03/13
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        res.append(celsius + 273.15)
        res.append(celsius * 1.80 + 32.00)
        return res