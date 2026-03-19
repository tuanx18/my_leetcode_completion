# [EASY] https://leetcode.com/problems/shuffle-string/
# Completed 2026/03/16
class Solution:
    @staticmethod
    def restoreString(s: str, indices: list[int]) -> str:
        ans = ["x"] * len(indices)
        for i, v in enumerate(indices):
            print(v, s[v])
            ans[v] = s[i]
        return ''.join(ans)
        
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol = Solution.restoreString(s, indices)
print(sol)