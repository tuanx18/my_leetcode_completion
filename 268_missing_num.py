class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # [0, 1,? (gap = 2), 3]
        if nums[0] == 1:
            return 0
        prev = None
        for i in nums:
            # First ID
            if prev is None and i == 0:
                prev = 0

            gap = i - prev
            prev = i

            # if gap == 0:
            #     return None

            if gap == 2:
                return i - 1
        return nums[-1] + 1