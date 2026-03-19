# [MEDIUM] https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i
# Completed 2026/02/23
class Solution(object):
    @staticmethod
    def maximumLength(s):
        """
        :type s: str
        :rtype: int
        """
        # get substr
        def sub(s, k):
            return [s[i:i+k] for i in range(len(s) - k + 1) if len(set(s[i:i+k])) == 1]

        if len(s) < 3:
            return -1

        n = len(s) - 2
        while n > 0:
            seen = {}
            subsets = sub(s, n)
            for j in subsets:
                seen[j] = seen.get(j, 0) + 1
                if seen[j] == 3:
                    return n
            n -= 1
        return -1

s = "abcdabcddddabcddddccccbbbbaaaa"
sol = Solution.maximumLength(s)
print(sol)