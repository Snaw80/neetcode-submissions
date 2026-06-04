"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newPointer = collections.defaultdict(lambda: Node(0))
        newPointer[None] = None

        current = head

        while current:
            newPointer[current].val = current.val
            newPointer[current].next = newPointer[current.next]
            newPointer[current].random = newPointer[current.random]

            current = current.next
        
        return newPointer[head]
