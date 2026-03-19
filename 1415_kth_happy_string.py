# [MEDIUM] https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
# Completed 2026/03/14
class Solution:
    def getHappyString(n: int, k: int) -> str:
        res = []
        path = []
        cha = ['a','b', 'c']

        def backtrack():
            if len(path) == n:
                res.append(''.join(path))
                return
            
            for i in cha:
                if not path:
                    path.append(i)
                    backtrack()
                    path.pop()
                else:
                    if path[-1] != i:
                        path.append(i)
                        backtrack()
                        path.pop()
                
        backtrack()
        print("LIST of ans: ", res)
        if k > len(res):
            return ""
        else:
            return res[k - 1]

n = 3
k = 9
sol = Solution.getHappyString(n, k)
print(sol)