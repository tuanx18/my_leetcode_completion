# [MEDIUM] https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Completed 2026/03/17
class Solution:
    @staticmethod
    def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
        idx = []
        for i, v in enumerate(groupSizes):
            idx.append((i, v))
        idx.sort(key=lambda x:x[1])
        # [(5, 1), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (6, 3)]
        stack = [idx[0][1]]
        res = []
        for tup in idx:
            if tup[1] == stack[0]:
                if len(stack) < stack[0] + 1:
                    stack.append(tup[0])
                else:
                    res.append(stack[1:])
                    stack = [tup[1], tup[0]]
            else:
                res.append(stack[1:])
                stack = [tup[1], tup[0]]
        res.append(stack[1:])
        return res

groupSizes = [3,4,3,3,4,4,3,4,3,3]
sol = Solution.groupThePeople(groupSizes)
print(sol)