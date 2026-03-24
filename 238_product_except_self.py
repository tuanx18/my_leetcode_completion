# [MEDIUM] https://leetcode.com/problems/product-of-array-except-self
# Completed 2026/03/24
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        curr = 1
        for i in nums:
            curr *= i
            prefix.append(curr)
        
        suffix = [1]
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr *= nums[i]
            suffix.append(curr)
        
        res = []
        for k in range(len(nums)):
            res.append(prefix[k] * suffix[len(nums) - 1 - k])
        return res
