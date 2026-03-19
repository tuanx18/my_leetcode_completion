# [MEDIUM] https://leetcode.com/problems/deepest-leaves-sum/
# Completed 2026/03/17

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            last_layer = []
            curr = len(queue)
            for i in range(curr):
                node = queue.pop(0)
                last_layer.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return sum(last_layer)