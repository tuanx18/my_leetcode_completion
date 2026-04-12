# [MEDIUM] https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii
# Completed 2026/04/11
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = {}
        idx = []
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = [i]
            else:
                freq[nums[i]].append(i)
        
        ans = float('inf')
        
        for k, v in freq.items():
            if len(v) >= 3:
                for j in range(2, len(v)):
                    ans = min(ans, 2 * (v[j] - v[j-2]))

        if ans == float('inf'):
            ans = -1
        return ans
        
        
nums = [1,2,1,1,3]
sol = Solution.minimumDistance(nums)
print(sol)