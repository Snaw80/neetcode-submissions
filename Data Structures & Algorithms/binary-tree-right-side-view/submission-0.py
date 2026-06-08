# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        r = []
        q = [root]

        while q:
            r.append(q[-1].val)
            q2 = []
            while q:
                elt = q.pop(0)

                if elt.left:
                    q2.append(elt.left)
                if elt.right:
                    q2.append(elt.right)
            q = q2
        return r
