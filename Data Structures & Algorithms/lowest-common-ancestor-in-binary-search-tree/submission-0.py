# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, p, q):
            v = node.val

            if v == p.val or v == q.val:
                return node

            if p.val < v and q.val < v:
                return dfs(node.left,p,q)
            elif p.val > v and q.val > v:
                return dfs(node.right,p,q)
            else:
                return node
        
        return dfs(root,p,q)
        