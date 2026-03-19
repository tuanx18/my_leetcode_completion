class Solution(object):
    @staticmethod
    def combinationSum3(k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []

        res = []
        path = []

        def backtrack():
            # if len(path) == k:
            if sum(path) == n and len(path) == k:
                srt = sorted(path)
                if srt not in res:
                    res.append(srt[:])
                return
            if sum(path) > n:
                return
            
            for i in range(1, 10):
                if i in path:
                    continue
                else:
                    path.append(i)
                    backtrack()
                    path.pop()

        backtrack()
        return res

k = 3
n = 9
sol = Solution.combinationSum3(k, n)
print(sol)