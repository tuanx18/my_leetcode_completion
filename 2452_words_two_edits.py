# [MEDIUM] https://leetcode.com/problems/words-within-two-edits-of-dictionary
# Completed 2026/04/22
class Solution:
    @staticmethod
    def twoEditWords(queries: list[str], dictionary: list[str]) -> list[str]:
        L = len(queries[0])
        res = []

        for q in queries:
            search = True
            for d in dictionary:
                if not search:
                    break
                dif = 0
                i = 0
                while i < L:
                    if q[i] != d[i]:
                        dif += 1
                    i += 1

                if dif <= 2:
                    res.append(q)
                    search = False
        return res

queries = ["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"]
dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]
# Expected ["tsl","yyy","rbc","dda","qus","hyb","ilu"]
sol = Solution.twoEditWords(queries, dictionary)
print(sol)