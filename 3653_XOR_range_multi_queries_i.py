# [MEDIUM] https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
# Completed 2026/04/08
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        res = nums[:]
        for q in queries:
            for i in range(q[0], q[1] + 1, q[2]):
                res[i] = (res[i] * q[3]) % (10 ** 9 + 7) 
        
        ans = res[0]
        for j in range(1, len(res)):
            ans ^= res[j]
        
        # print(res)
        
        return ans