# [MEDIUM] https://leetcode.com/problems/closest-equal-element-queries
# Completed 2026/04/16
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from bisect import bisect_left

        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = []
            freq[nums[i]].append(i)

        l = len(nums)
        res = []

        for q in queries:

            pos_list = freq[nums[q]]

            if len(pos_list) == 1:
                res.append(-1)
                continue

            # find index of q inside pos_list
            idx = bisect_left(pos_list, q)

            left = pos_list[idx - 1] if idx > 0 else pos_list[-1]
            right = pos_list[idx + 1] if idx < len(pos_list) - 1 else pos_list[0]

            dist_left = min(abs(q - left), l - abs(q - left))
            dist_right = min(abs(q - right), l - abs(q - right))

            res.append(min(dist_left, dist_right))

        return res