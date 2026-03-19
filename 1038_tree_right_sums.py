# [MEDIUM] https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Completed 2026/03/12
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.running_sum += node.val
            node.val = self.running_sum
            
            dfs(node.left)
        dfs(root)
        return root