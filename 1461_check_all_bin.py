# [MEDIUM] https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
# Completed 2026/02/23
class Solution(object):
    def hasAllCodes(s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        def grey_code(a):
            return [format((x ^ (x >> 1)), '0{}b'.format(a)) for x in range(1 << a)]

        bina = set(grey_code(k))
        subsets = [s[i:i+k] for i in range(len(s) - k + 1)]

        for sub in subsets:
            if sub in bina:
                bina.remove(sub)
        if len(bina) == 0:
            return True
        else:
            return False
        
s = '00110110'
k = 2
sol = Solution.hasAllCodes(s, k)
print(sol)