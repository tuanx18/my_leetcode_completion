# [EASY] https://leetcode.com/problems/product-of-array-except-self
# Completed 2026/02/22
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        first_pass = [1]
        for i in range(1, len(nums)):
            prod = first_pass[-1] * nums[i - 1]
            first_pass.append(prod)
        print(first_pass)

        res = [0] * len(nums)
        curr = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = first_pass[j] * curr
            curr *= nums[j]
        return res