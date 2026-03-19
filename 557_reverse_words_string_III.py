# [EASY] https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Completed 2026/03/18
class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        words = s.split()
        ans = ''
        for w in words:
            curr = ''
            for ch in w:
                # print(ch)
                curr = ch + curr
            ans += curr
            ans += ' '
        return ans

s = "Let's take LeetCode contest"
sol = Solution.reverseWords(s)
print(sol)