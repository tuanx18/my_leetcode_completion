# [EASY] https://leetcode.com/problems/path-sum/
# Completed 2026/02/24
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        res = []

        def backtrack(node, running):
            if not node:
                return
            
            running += node.val
            if not node.left and not node.right:
                if running == targetSum:
                    res.append("x")
                running -= node.val
                return

            if node.left:
                backtrack(node.left, running)
            if node.right:
                backtrack(node.right, running)
            running -= node.val
        backtrack(root, 0)
        if res:
            return True
        else:
            return False

            
        