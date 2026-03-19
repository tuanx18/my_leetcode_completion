# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
# Completed 2026/02/24
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        nums = []
        def dfs(node, bnr):
            bnr += str(node.val)

            if not node.left and not node.right:
                # nums.append(int(bnr, 2))
                nums.append(int(bnr, 2))
                return

            if node.left: dfs(node.left, bnr)
            if node.right: dfs(node.right, bnr)
        dfs(root, '')
        return sum(nums)
