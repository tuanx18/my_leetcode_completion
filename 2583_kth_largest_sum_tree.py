# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        level = 0
        curr = 1
        sum_current = 0
        level_sum_list = []
        queue = [root]
        while queue:
            if curr == 0 and sum_current is not None:
                level_sum_list.append(sum_current)
                sum_current = 0
                curr = len(queue)
                level += 1

            node = queue.pop(0)
            sum_current += node.val
            curr -= 1

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        level_sum_list.append(sum_current)
        level_sum_list.sort()
        if k > level + 1:
            return -1
        return level_sum_list[-k]


        