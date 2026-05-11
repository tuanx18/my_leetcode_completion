# [EASY] https://leetcode.com/problems/count-indices-with-opposite-parity
# Completed 2026/05/05
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res = []
        odd = 0
        even = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 0:
                res.append(odd)
                even += 1
            else:
                res.append(even)
                odd += 1
        res.reverse()
        return res
