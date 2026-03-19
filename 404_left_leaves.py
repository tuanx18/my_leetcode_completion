# [EASY] https://leetcode.com/problems/sum-of-left-leaves
# Completed 2026/03/04
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        res = 0
        while queue:
            node = queue.pop(0)

            if node.left: 
                queue.append(node.left)
                if not node.left.left and not node.left.right:
                    res += node.left.val
            if node.right:
                queue.append(node.right)
        return res