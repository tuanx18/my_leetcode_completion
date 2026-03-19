# [EASY] https://leetcode.com/problems/find-indices-of-stable-mountains/
# Completed 2026/03/17
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        for i in range(len(height)):
            if i != 0:
                if height[i-1] > threshold:
                    res.append(i)
        return res