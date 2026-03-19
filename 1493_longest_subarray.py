# [MEDIUM] https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
# Completed 2026/03/01

class Solution(object):
    @staticmethod
    def longestSubarray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_streak = 0
        if nums[0] == 1:
            curr_streak = 1
        else:
            curr_streak = 0
        max_streak = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] == 1:
                curr_streak += 1
            elif nums[i] == nums[i - 1] == 0:
                prev_streak = 0
            elif nums[i] == 1 and nums[i - 1] == 0:
                max_streak = max(max_streak, curr_streak + prev_streak)
                curr_streak = 1
            elif nums[i] == 0 and nums[i - 1] == 1:
                max_streak = max(max_streak, curr_streak + prev_streak)
                prev_streak = curr_streak
                curr_streak = 0
        max_streak = max(max_streak, curr_streak + prev_streak)
        if max_streak == len(nums):
            max_streak -= 1
        return max_streak

nums = [1,0,0,1,0]
# Output: 5
sol = Solution.longestSubarray(nums)
print(sol)
        