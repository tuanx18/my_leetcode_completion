class Solution(object):
    @staticmethod
    def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uni = set(nums)
        n = list(uni)
        n.sort(reverse=True)
        if len(n) <= 2:
            return n[0]
        return n[2]

nums = [-3,-2,-1,0]
x = Solution.thirdMax(nums)
print(x)