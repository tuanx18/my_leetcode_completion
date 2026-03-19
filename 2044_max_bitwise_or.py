# [MEDIUM] 
# Completed 2026/03/15
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for i in nums:
            mx = mx | i
        n = len(nums)
        res = 0

        def backtrack(i, cur_or):
            nonlocal res

            if i == n:
                if cur_or == mx:
                    res += 1
                return

            backtrack(i+1, cur_or | nums[i])
            backtrack(i+1, cur_or)
        backtrack(0, 0)
        return res
        