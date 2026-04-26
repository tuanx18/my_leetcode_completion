# [MEDIUM] https://leetcode.com/problems/maximum-binary-tree
# Completed 2026/04/22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(n):
            if len(n) == 0:
                return None
            
            mi = n.index(max(n))
            root = TreeNode(n[mi])

            left = n[:mi]
            right = n[mi+1:]

            root.left = build(left)
            root.right = build(right)

            return root
        
        ans = build(nums)
        return ans