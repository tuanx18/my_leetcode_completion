# [EASY] https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Completed 2026/05/02
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        def sub(num, k):
            i = 0
            j = k
            dist = 0
            while j <= len(num):
                x = len(set(num[i:j])) ** 2
                dist += x
                i += 1
                j += 1
            return dist
        
        res = 0
        for i in range(1, len(nums) + 1):
            cur = sub(nums, i)
            res += cur
        return res