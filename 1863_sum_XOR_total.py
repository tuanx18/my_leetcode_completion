# [EASY] https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# Completed 2026/03/23
class Solution:
    @staticmethod
    def subsetXORSum(nums: list[int]) -> int:
        res = 0
        path = []
        n = len(nums)

        def backtrack(i):
            nonlocal res
            if i == n:
                if not path:
                    pass
                else:
                    curr = path[0]
                    if len(path) > 1:
                        for k in path[1:]:
                            curr ^= k
                    res += curr
                return
                        
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
        backtrack(0)
        return res

nums = [1,3]
sol = Solution.subsetXORSum(nums)
print(sol)