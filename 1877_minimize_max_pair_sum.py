# [MEDIUM] https://leetcode.com/problems/minimize-maximum-pair-sum-in-array
#
class Solution:
    @staticmethod
    def minPairSum(nums: list[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l < r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans

nums = [4,1,5,1,2,5,1,5,5,4]
sol = Solution.minPairSum(nums)
print(sol)