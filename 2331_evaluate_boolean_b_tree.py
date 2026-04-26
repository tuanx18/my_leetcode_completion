# [EASY] https://leetcode.com/problems/evaluate-boolean-binary-tree/
# Completed 2026/04/26

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def eva(node: TreeNode):
            if not node.left:
                if node.val == 0:
                    return False
                else:
                    return True
            
            if node.val == 2:
                return eva(node.left) | eva(node.right)
            
            if node.val == 3:
                return eva(node.left) & eva(node.right)
        
        return eva(root)