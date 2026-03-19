class Solution(object):
    @staticmethod
    def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        for ind, val in enumerate(nums):
            if val in window:
                return True
            window.add(val)
            if len(window) > k:
                window.remove(nums[ind - k])
        return False
    
nums = [1,2,3,4,5,6,7,8,9,9]
k = 3
x = Solution.containsNearbyDuplicate(nums, k)
print("CASE 1: ", x)
        
nums = [1,2,3,1,2,3]
k = 2
x = Solution.containsNearbyDuplicate(nums, k)
print("CASE 2: ", x)