# [EASY] https://leetcode.com/problems/check-balanced-string/
# Completed 2026/04/07
class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        snum = str(num)
        for i in range(len(snum)):
            if i % 2 == 0:
                even += int(snum[i])
            else:
                odd += int(snum[i])
        if odd == even:
            return True
        else:
            return False