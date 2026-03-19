# [EASY] https://leetcode.com/problems/longest-harmonious-subsequence
# Completed 2026/03/14
class Solution:
    @staticmethod
    def findLHS(nums: list[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        print(freq)
        ans = 0
        for k, v in freq.items():
            # print(k, freq.get(k + 1))
            if freq.get(k + 1, 0) != 0:
                ans = max(ans, freq[k] + freq[k+1])
        return ans
    
nums = [1,2,2,1]
sol = Solution.findLHS(nums)
print(sol)