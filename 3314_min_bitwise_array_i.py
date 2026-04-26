# [EASY] https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
# Completed 2026/04/25
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        def find_x(n):
            for x in range(n):
                if x | (x + 1) == n:
                    return x
            return -1
        
        res = []
        for i in nums:
            res.append(find_x(i))
        
        return res