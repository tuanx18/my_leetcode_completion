# [HARD] https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
# 
class Solution(object):
    @staticmethod
    def sumCounts(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = {}
            distinct = 0

            for j in range(i, n):
                val = nums[j]
                if val not in freq:
                    freq[val] = 1
                    distinct += 1
                else:
                    freq[val] += 1
                ans += distinct * distinct
        return ans % MOD 
    
nums = [2,2]
sol = Solution.sumCounts(nums)
print(sol)