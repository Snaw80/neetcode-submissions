# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        l2 = slow.next
        prev = None
        slow.next = None
        while l2:
            t = l2.next
            l2.next = prev
            prev = l2
            l2 = t
        
        l1,l2 = head, prev
        while l2:
            t1,t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1 = t1
            l2 = t2
        