# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        queue = [original]
        queue_sol = [cloned]
        while queue:
            node = queue.pop(0)
            node_s = queue_sol.pop(0)
            if node is target:
                return node_s

            if node.left: 
                queue.append(node.left)
                queue_sol.append(node_s.left)
            if node.right: 
                queue.append(node.right)
                queue_sol.append(node_s.right)