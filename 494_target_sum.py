class Solution(object):
    @staticmethod
    def findTargetSumWays(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        def dfs(i, total):
            if i == n:
                if total == target:
                    return 1
                else:
                    return 0
            
            way_plus = dfs(i + 1, total + nums[i])
            way_minus = dfs(i + 1, total - nums[i])
            return way_minus + way_plus
        res = dfs(0, 0)
        return res
        
nums = [42,1,42,35,33,37,26,3,23,29,22,50,34,31,11,28,20,31,32,28]
target = 2
sol = Solution.findTargetSumWays(nums, target)
print(sol)