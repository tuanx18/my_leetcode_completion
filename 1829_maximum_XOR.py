# [MEDIUM] https://leetcode.com/problems/maximum-xor-for-each-query/
# Completed 2026/03/17
class Solution:
    @staticmethod
    def getMaximumXor(nums: list[int], maximumBit: int) -> list[int]:
        # target = (1 << maximumBit) - 1
        # output = []
        # print(target)
        # for i in range(len(nums), 0, -1):
        #     test = []
        #     sub = nums[0:i]
        #     for z in range(len(sub)):
        #         test.append(sub[z])
        #         if z == 0:
        #             item = sub[z]
        #         else:
        #             item ^= sub[z]
        #     print(test)
        #     output.append(item ^ target)
        # return output
        target = (1 << maximumBit) - 1        
        for i in range(len(nums)):
            if i == 0:
                curr = nums[i]
            else:
                curr ^= nums[i]
        res = []
        r = len(nums) - 1
        while r >= 0:
            res.append(curr ^ target)
            curr ^= nums[r]
            r -= 1
        return res

nums = [0,1,1,3]
maximumBit = 2
# Output: [0,3,2,3]
sol = Solution.getMaximumXor(nums, maximumBit)
print(sol)

# print(56 ^ 17 ^ 23) # 62
# print(56 ^ 17) # 41
# # how to get 23 when there is 62
# print(56 ^ 17 ^ 62)