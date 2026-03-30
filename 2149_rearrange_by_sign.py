# [MEDIUM] https://leetcode.com/problems/rearrange-array-elements-by-sign/
# Completed 2026/03/30
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        for x in range(len(pos)):
            res.append(pos[x])
            res.append(neg[x])
        return res