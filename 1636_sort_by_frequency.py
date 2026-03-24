# [EASY] https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Completed 2026/03/24
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        new = []
        for k, v in freq.items():
            new.append((k, v))
        new.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        for i in new:
            for x in range(i[1]):
                res.append(i[0])
        return res