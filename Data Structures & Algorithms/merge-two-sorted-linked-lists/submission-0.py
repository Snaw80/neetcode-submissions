# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        head = None

        pre = None
        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val > current2.val:
                t = current2.next
                if pre:
                    pre.next = current2
                current2.next = current1
                pre = current2
                current2 = t
                if not head or head.val == current1.val:
                    head = pre
            else:
                if not head:
                    head = current1
                pre = current1
                current1 = current1.next
        

        if not head:
            if current1:
                head = current1
            else:
                head = current2
                
        while current2:
            if pre:
                pre.next = current2
            pre = current2
            current2 = current2.next
        
        return head