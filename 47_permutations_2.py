class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        n = len(nums)

        used = [False] * n

        def backtrack():
            if len(path) == n and path not in res:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res