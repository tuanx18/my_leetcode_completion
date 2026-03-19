# [EASY] https://leetcode.com/problems/set-mismatch/?envType=problem-list-v2&envId=bit-manipulation
# Completed 2026/02/22

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # find missing
        desired = set(range(1, len(nums) + 1))
        st = set(nums)
        missing = desired - st
        missing_value = next(iter(missing))

        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                duplicated = nums[i]
        
        res = [duplicated, missing_value]
        return res
