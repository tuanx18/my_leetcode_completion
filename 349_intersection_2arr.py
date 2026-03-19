class Solution(object):
    @staticmethod
    def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        i = s1.intersection(s2)
        return i

nums1 = [1,2,2,1]
nums2 = [2,2]
x = Solution.intersection(nums1, nums2)
print(x)