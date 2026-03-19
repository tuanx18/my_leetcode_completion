# [EASY] https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
# Completed 2026/02/21

class Solution(object):
    @staticmethod
    def findTheLongestBalancedSubstring(s):
        """
        :type s: str
        :rtype: int
        """
                
        if not s:
                    return 0

        # Build (char, count) runs, e.g., "001110" -> [('0',2), ('1',3), ('0',1)]
        runs = []
        prev = None
        count = 0
        for ch in s:
            if prev is None or ch == prev:
                count += 1
                prev = ch
            else:
                runs.append((prev, count))
                prev = ch
                count = 1
        runs.append((prev, count))  # last run

        # Only 0-then-1 adjacent runs form balanced substrings
        max_counter = 0
        for i in range(1, len(runs)):
            c0, n0 = runs[i - 1]
            c1, n1 = runs[i]
            if c0 == '0' and c1 == '1':
                max_counter = max(max_counter, 2 * min(n0, n1))

        return max_counter


s = "010"
sol = Solution.findTheLongestBalancedSubstring(s) # 1 1 3 3
print(sol)