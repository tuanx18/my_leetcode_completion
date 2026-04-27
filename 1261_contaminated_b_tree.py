# [MEDIUM] https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree
# Completed 2026/04/27

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.cont = root
        self.items = [0]

        root.val = 0
        queue = [root]

        while queue:
            node = queue.pop(0)
            curr = node.val

            if node.left:
                node.left.val = curr * 2 + 1
                self.items.append(node.left.val)
                queue.append(node.left)
            
            if node.right:
                node.right.val = curr * 2 + 2
                self.items.append(node.right.val)
                queue.append(node.right)


    def find(self, target: int) -> bool:
        if target in self.items:
            return True
        else:
            return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)