# [MEDIUM]
# Completed 2026/03/01
class Solution:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])

        l = 0
        r = k
        curr = 0

        for ch in s[l:r]:
            if ch in vowels:
                curr += 1
            ans = curr
        l += 1
        r += 1

        while r <= len(s):
            if s[r-1] in vowels:
                curr += 1
            if s[l-1] in vowels:
                curr -= 1
            ans = max(ans, curr)
            l += 1
            r += 1
        return ans
    
s = "abciiidef"
k = 3
sol = Solution.maxVowels(s, k)
print(sol)