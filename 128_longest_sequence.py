class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_set = set(nums)
        seen = set()
        max_seq = 1
        for i in nums:
            if i in seen:
                continue
            if (i - 1) in nums_set:
                continue
            
            seen.add(i)
            seq = 1
            looking_for = i + 1
            while looking_for in nums_set:
                seq += 1
                looking_for += 1
                max_seq = max(seq, max_seq)
        return max_seq