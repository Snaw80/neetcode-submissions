# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            r = 0
            if not node:
                return 0
            new_m = m
            if node.val >= m:
                r = 1
                new_m = node.val
            lr = dfs(node.left,new_m)
            rr = dfs(node.right,new_m)
            return r + lr + rr

        return dfs(root, -100)