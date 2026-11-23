class Node:
    def __init__(self, key, value):
        self.key =  key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
# 不懂
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
