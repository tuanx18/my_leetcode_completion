# [MEDIUM] https://leetcode.com/problems/max-consecutive-ones-iii
# Completed 2026/02/28
class Solution(object):
    @staticmethod
    def longestOnes(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rem = k
        best = 0
        start = 0

        for id, val in enumerate(nums):
            if val == 0:
                rem -= 1

            while rem < 0:
                if nums[start] == 0:
                    rem += 1
                start += 1
            
            best = max(best, id - start + 1)

        return best

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
sol = Solution.longestOnes(nums, k)
print(sol)