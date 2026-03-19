# [EASY] https://leetcode.com/problems/left-and-right-sum-differences
# Completed 2026/02/23
class Solution(object):
    def leftRightDifference(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums) - 1
        left_sum = right_sum = 0
        res_l = [0] * len(nums)
        res_r = [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            res_l[left] += left_sum
            res_r[right] += right_sum

            left_sum += nums[left]
            right_sum += nums[right]

            left += 1
            right -= 1
        
        for j in range(len(nums)):
            res[j] = abs(res_l[j] - res_r[j])

        return res

nums = [10,4,8,3]
# Output: [15,1,11,22]
sol = Solution.leftRightDifference(nums)
print(sol)