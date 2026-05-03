# [MEDIUM] https://leetcode.com/problems/divide-array-into-arrays-with-max-difference
# Completed 2026/05/03
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i-2] > k:
                return res
        
        for i in range(0, len(nums), 3):
            res.append(nums[i:i+3])
        return res