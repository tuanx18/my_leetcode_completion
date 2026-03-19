# [MEDIUM] https://leetcode.com/problems/path-sum-ii/description/
# Completed 2026/02/24
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        path = []
        res = []

        def backtrack(node):
            if not node:
                return
            
            path.append(node.val)

            if not node.left and not node.right:
                if sum(path) == targetSum:
                    res.append(path[:])
                path.pop()
                return

            if node.left: 
                backtrack(node.left)

            if node.right:
                backtrack(node.right)
            path.pop()

        backtrack(root)
        return res
        