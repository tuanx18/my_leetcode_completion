class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] >= nums[i]:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)
        return max_sum