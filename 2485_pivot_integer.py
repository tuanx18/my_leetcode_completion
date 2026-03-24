# [EASY]
# Completed 2026/03/24
class Solution:
    @staticmethod
    def pivotInteger(n: int) -> int:
    
        tot = 0
        for i in range(n + 1):
            tot += i

        tot_left = 0
        for i in range(1, n + 1):
            tot_left += i      # include i on the left
            tot -= i           # exclude i from the right

            if tot_left == tot + i:   # check pivot condition
                return i
        
        return -1

n = 3
sol = Solution.pivotInteger(n)
print(sol)