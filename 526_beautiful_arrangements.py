# [MEDIUM] https://leetcode.com/problems/beautiful-arrangement
# Completed 2026/03/13
class Solution:
    def countArrangement(self, n: int) -> int:
        res = []
        path = []

        used = [False] * n

        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return
            
            for j in range(0, n):
                if used[j]:
                    continue
                
                if ((len(path) + 1) % (j + 1) == 0) or ((j + 1) % (len(path) + 1) == 0):
                    used[j] = True
                    path.append(j + 1)

                    backtrack()
                    path.pop()
                    used[j] = False
        backtrack()
        return len(res)
            
            

#