class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_indices = []
        for id1, item in enumerate(nums):
            remain_num = target - item
            for id2, item2 in enumerate(nums):
                if id1 == id2:
                    pass
                elif item2 == remain_num and id1 not in list_indices:
                    new_list = [id1, id2]
                    list_indices.extend(new_list)
        return list_indices