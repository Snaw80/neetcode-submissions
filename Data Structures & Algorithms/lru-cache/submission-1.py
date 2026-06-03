class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _delete(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        
        node = self.hm[key]

        self._delete(node)
        self._add(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self._delete(node)
            self._add(node)
        
        else:
            node = Node(key,value)
            self.hm[key] = node
            self._add(node)
            self.size += 1
        
        if self.size > self.capacity:
            t = self.head.next
            self._delete(t)
            self.size -= 1
            del self.hm[t.key]
        