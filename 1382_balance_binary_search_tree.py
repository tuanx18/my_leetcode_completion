# [MEDIUM] https://leetcode.com/problems/balance-a-binary-search-tree/
# Completed 2026/04/22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        flat = []
        while queue:
            node = queue.pop(0)
            flat.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        flat.sort()
        
        def balance(nums):
            if len(nums) == 0:
                return None
            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid+1:]

            root = TreeNode(nums[mid])
            root.left = balance(l)
            root.right = balance(r)
            return root
        
        res = balance(flat)
        return res