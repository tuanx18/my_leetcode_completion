# https://leetcode.com/problems/maximum-69-number/
# Completed 2026/03/24
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = [ch for ch in str(num)]
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        res = ''.join(s)
        return int(res)