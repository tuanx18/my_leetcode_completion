# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        def dfs(node):
            if not node.left and not node.right:
                return

            if node.left and not node.right:
                node.right = node.left
                node.left = None
            elif node.right and not node.left:
                node.left = node.right
                node.right = None
                
            if node.left and node.right:
                node.left, node.right = node.right, node.left
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        dfs(root)
        return root
