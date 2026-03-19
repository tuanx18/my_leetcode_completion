# [MEDIUM] https://leetcode.com/problems/find-unique-binary-string
# Completed 2026/03/08
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        seen = set(nums)
        n = len(nums[0])
        res = []
        path = []
        
        def backtrack():
            if len(path) == n:
                s = ''.join(path)
                if s not in seen and not res:
                    res.append(s)
                return

            if res:
                return

            path.append("0")
            backtrack()
            path.pop()

            if res:
                return

            path.append("1")
            backtrack()
            path.pop()
        backtrack()
        return res[0]