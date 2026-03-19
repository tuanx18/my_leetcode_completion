# [MEDIUM] https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/
# Completed 2026/03/14
class Solution:
    def validStrings(self, n: int) -> List[str]:
        path = []
        res = []

        def backtrack():
            if len(path) == n:
                res.append(''.join(path))
                return
            
            for i in ['0', '1']:
                if not path:
                    path.append(i)
                    backtrack()
                    path.pop()
                else:
                    if path[-1] == '0' and i == '0':
                        pass
                    else:
                        path.append(i)
                        backtrack()
                        path.pop()
        backtrack()
        return res