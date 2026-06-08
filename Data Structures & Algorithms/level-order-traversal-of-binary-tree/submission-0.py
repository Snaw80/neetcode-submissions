# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r = []
        q = []

        q.append(root)

        while q:
            level = []
            q2 = []
            while q:
                elt = q.pop(0)
                level.append(elt.val)

                if elt.left:
                    q2.append(elt.left)
                if elt.right:
                    q2.append(elt.right)
                    
            q = q2
            r.append(level)

        return r