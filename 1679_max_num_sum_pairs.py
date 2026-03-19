# [MEDIUM] https://leetcode.com/problems/max-number-of-k-sum-pairs
# Completed 2026/02/24
class Solution(object):
    @staticmethod
    def maxOperations(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 0

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                ans += 1
                right -= 1
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return ans

nums = [3,1,3,4,3]
k = 6
sol = Solution.maxOperations(nums,k)
print(sol)
