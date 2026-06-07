# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = []
        q2 = []

        q1.append(p)
        q2.append(q)

        while q1 and q2:
            elt1 = q1.pop()
            elt2 = q2.pop()

            if not (elt1 or elt2):
                continue

            if not elt1 or not elt2 or elt1.val != elt2.val:
                return False
            
            q1.append(elt1.left)
            q1.append(elt1.right)

            q2.append(elt2.left)
            q2.append(elt2.right)
        
        return not (q1 or q2)