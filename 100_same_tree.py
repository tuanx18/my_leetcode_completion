# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def bfs(node):
            queue = [node]
            res = []
            while queue:
                node = queue.pop(0)
                if not node:
                    res.append("Nan")
                    continue
                
                val = node.val
                res.append(val)
                queue.append(node.left)
                queue.append(node.right)
            return res
        
        lst_p = bfs(p)
        lst_q = bfs(q)
        return lst_p == lst_q
    
    def isSameTree_optimal(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
            

        