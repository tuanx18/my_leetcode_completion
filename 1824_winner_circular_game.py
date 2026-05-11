# [MEDIUM] https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Completed 2026/05/04
class Solution:
    @staticmethod
    def findTheWinner(n: int,k: int) -> int:
        pol = [z for z in range(n)]
        tot = set(pol[:])
        seen = set()

        x = 0
        roll = k - 1

        while len(seen) < n - 1:
            x += 1
            
            while (x % n) in seen:   # 🔧 FIX: use index directly, no need for pol[]
                x += 1

            roll -= 1   # 🔧 FIX: move decrement AFTER confirming this is an alive person

            if roll <= 0:
                seen.add(x % n)   # 🔧 FIX: use index directly instead of pol[x % n]
                roll = k - 1      # 🔧 FIX: reset to k - 1, not k

        res = tot - seen
        r = next(iter(res))
        return r + 1

n = 3
k = 1
sol = Solution.findTheWinner(n, k)
print(sol)