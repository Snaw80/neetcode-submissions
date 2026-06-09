# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def dfs(node, k):
            nonlocal res
            if not node:
                return 0
            
            s = dfs(node.left,k) + 1
            if s == k:
                res = node.val
                return s
            s += dfs(node.right,k-s)
            return s
        
        dfs(root,k)

        return res