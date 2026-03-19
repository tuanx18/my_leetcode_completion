# [MEDIUM] https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
# Completed 2026/03/17
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # new_mat = []
        # freq = {}
        # for i in nums:
        #     freq[i] = freq.get(i, 0) + 1
        
        # while freq:
        #     curr_level = []
        #     for key in freq.keys():
        #         freq[key] -= 1
        #         curr_level.append(key)
        #         if freq[key] == 0:
        #             freq.pop(key)
        #     new_mat.append(curr_level)
        # return new_mat
        res = []
        while nums:
            to_add = []
            new_arr = []
            seen = set()
            for i in nums:
                if i not in seen:
                    seen.add(i)
                    to_add.append(i)
                else:
                    new_arr.append(i)
            res.append(to_add)
            nums = new_arr.copy()
        return res