# [EASY] https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Completed 2026/05/04
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for i, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
        
        lst = []
        for k, v in freq.items():
            lst.append((k, v))
        lst.sort(key = lambda x: x[1], reverse=True)

        res = 0
        val = lst[0][1]
        for k, v in lst:
            if v != val:
                break
            res += v
        return res