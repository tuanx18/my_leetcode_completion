# [EASY] https://leetcode.com/problems/count-the-number-of-consistent-strings/
# Completed 2026/03/23
class Solution:
    @staticmethod
    def countConsistentStrings(allowed: str, words: list[str]) -> int:
        res = 0
        for w in words:
            # print(w)
            seen = set()
            up = True
            for ch in w:
                if ch in allowed:
                    print("found", ch, allowed)
                    seen.add(ch)
                else:
                    up = False
                    break
            if up: res += 1
        return res

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
sol = Solution.countConsistentStrings(allowed, words)
print(sol)