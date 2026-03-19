# [EASY] https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string
# Completed 2026/03/05
class Solution:
    def minOperations(self, s: str) -> int:
        ans = 2000000
        swap = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    swap += 1
            elif i % 2 == 1:
                if s[i] == '0':
                    swap += 1
        ans = min(ans, swap)

        swap = 0
        for i in range(len(s)):
            if i % 2 == 1:
                if s[i] == '1':
                    swap += 1
            elif i % 2 == 0:
                if s[i] == '0':
                    swap += 1
        ans = min(ans, swap)
        return ans