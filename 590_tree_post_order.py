# [EASY] https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Completed 2026/04/18
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            
            for child in node.children:
                dfs(child)

            res.append(node.val)
        dfs(root)
        return res