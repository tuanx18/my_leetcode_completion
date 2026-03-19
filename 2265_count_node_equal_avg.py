# [MEDIUM] https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree
# Completed 2026/03/18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0

            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            
            subsum = lsum + rsum + node.val
            subcnt = lcnt + rcnt + 1
            if subsum // subcnt == node.val:
                ans += 1

            return subsum, subcnt
        dfs(root)
        return ans