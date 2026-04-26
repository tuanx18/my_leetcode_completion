# [EASY] https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements
# Completed 2026/04/25
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        def av(a, b):
            return (a + b) / 2

        while nums:
            ia = nums.index(min(nums))
            ib = nums.index(max(nums))
            if ia < ib:
                ia, ib = ib, ia
            a = nums.pop(ia)
            b = nums.pop(ib)
            averages.append(av(a, b))
        
        return min(averages)