class Solution(object):
    @staticmethod
    def findLongestChain(pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        nums = [x[0] for x in pairs]
        nums.sort()
        max_streak = 0
        for i in range(len(nums) - 1):
            streak = 1
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] >= 2:
                    streak += 1
                    max_streak = max(max_streak, streak)
                    print(max_streak)
        return max_streak

pairs = [[1,2],[2,3],[3,4]]
x = Solution.findLongestChain(pairs)
print(x)
        