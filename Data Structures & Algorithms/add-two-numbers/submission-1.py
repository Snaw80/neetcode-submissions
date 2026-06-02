# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current1 = l1
        current2 = l2

        r = ListNode()
        head = r

        while current1 or current2 or carry:
            elt1 = 0
            if current1:
                elt1 = current1.val
                current1 = current1.next
            elt2 = 0
            if current2:
                elt2 = current2.val
                current2 = current2.next
            new = elt1 + elt2 + carry
            carry = new // 10
            r.next = ListNode(new % 10)
            r = r.next
        
        return head.next
            