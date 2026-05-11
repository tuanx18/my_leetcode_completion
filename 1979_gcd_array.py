# [EASY] https://leetcode.com/problems/find-greatest-common-divisor-of-array
# Completed 2026/05/04
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return gcd(min(nums), max(nums))