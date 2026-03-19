# [MEDIUM] https://leetcode.com/problems/smallest-all-ones-multiple/
#

class Solution(object):
    @staticmethod
    def minAllOneMultiple(k):
        """
        :type k: int
        :rtype: int
        """
        
        if k % 2 == 0 or k % 5 == 0:
            return -1
        rem = 0
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            print(f"len={length}, remainder={rem}")  # <-- watch it evolve
            if rem == 0:
                return length
        return -1

    
k = 17
sol = Solution.minAllOneMultiple(k)
print(sol)