# [EASY] https://leetcode.com/problems/defanging-an-ip-address/
# Completed 2026/03/13
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''
        for ch in address:
            if ch == '.':
                ans += '[.]'
            else:
                ans += ch
        return ans