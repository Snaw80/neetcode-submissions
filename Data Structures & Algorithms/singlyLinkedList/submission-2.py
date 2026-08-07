class Node:

    def __init__(self, value):
        self.val = value
        self.link = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head
        while index > 0 and current:
            current = current.link
            index -= 1
        
        if not current:
            return -1
        return current.val

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.link = self.head
        self.head = new
        if not new.link:
            self.tail = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
            self.tail = new
            return
        
        self.tail.link = new
        self.tail = new

    def remove(self, index: int) -> bool:
        if not index:
            if not self.head:
                return False
            self.head = self.head.link
            return True
        
        current = self.head
        while index > 1 and current:
            current = current.link
            index -= 1
        
        if not current or not current.link:
            return False
        
        if current.link == self.tail:
            self.tail = current
        current.link = current.link.link
        return True


    def getValues(self) -> List[int]:
        l = []
        current = self.head

        while current:
            l.append(current.val)
            current = current.link
        
        return l
